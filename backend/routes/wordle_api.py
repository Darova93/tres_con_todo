from dataclasses import dataclass
from typing import cast
from flask import Blueprint, jsonify, request
from flask_cors import cross_origin
from marshmallow import Schema, ValidationError
from marshmallow.fields import String, Nested, List, Integer
from marshmallow.validate import Length, Regexp

from games.wordle.wordle import Wordle, WordleTurn, GameStatus
from games.wordle.file_word_picker import FileWordPicker


app_route = Blueprint('wordle', __name__, url_prefix="/v0.1/wordle")


class WordleCheckWordRequestWord(Schema):
    word = String(required=True, validate=[Regexp("^[a-zA-Z]{5}$")])
    correct = List(Integer(), required=True)
    fails = List(Integer(), required=True)
    missplaced = List(Integer(), required=True)

class WordleCheckWordRequest(Schema):
    status = String(required=True, validate=Length(max=100))
    words = List(Nested(WordleCheckWordRequestWord(), required=True))

@dataclass
class WordleCheckWordResponseTurn:
    correct: list[int]
    fails: list[int]
    missplaced: list[int]
    word: str

    def __init__(self, turn: WordleTurn):
        self.correct = turn.correct_letter_indices
        self.fails = turn.incorrect_letter_indices
        self.missplaced = turn.missplaced_letter_indices
        self.word = turn.player_guess

@dataclass
class WordleCheckWordResponse:
    status: GameStatus
    words: list[WordleCheckWordResponseTurn]

    def __init__(self, wordle: Wordle):
        self.status = wordle.get_game_status()
        self.words = [WordleCheckWordResponseTurn(turn) for turn in wordle.turns]

@app_route.route("/checkword", methods=["POST"])
@cross_origin()
def check_word():
    try:
        check_word_request = cast(dict, WordleCheckWordRequest().load(request.get_json()))
        wordle = Wordle(FileWordPicker())
        for word_attempt in check_word_request["words"]:
            wordle.guess(word_attempt["word"])
        wordle_response = WordleCheckWordResponse(wordle)
        return jsonify(wordle_response)
    except ValidationError as error:
        return error.messages, 400


