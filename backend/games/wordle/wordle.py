from dataclasses import dataclass, field
from games.wordle.types import GameStatus, WordPicker


@dataclass
class WordleTurn:
    word_of_the_day: str
    player_guess: str
    correct_letter_indices: list[int] = field(default_factory=list)
    incorrect_letter_indices: list[int] = field(default_factory=list)
    missplaced_letter_indices: list[int] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.word_of_the_day = self.word_of_the_day.upper()
        self.player_guess = self.player_guess.upper()
        answer_letter_count = {letter : self.word_of_the_day.count(letter) for letter in set(self.word_of_the_day)}
        self.__compute_correct_letter_indices(answer_letter_count)
        self.__compute_missplaced_and_wrong_letter_indices(answer_letter_count)

    def __compute_correct_letter_indices(self, answer_letter_count: dict[str, int]) -> None:
        for index, letter in enumerate(self.word_of_the_day):
            if self.player_guess[index] == letter:
                self.correct_letter_indices.append(index)
                answer_letter_count[self.player_guess[index]] -= 1

    def __compute_missplaced_and_wrong_letter_indices(self, answer_letter_count: dict[str, int]) -> None:
        for index, letter in enumerate(self.word_of_the_day):
            if self.player_guess[index] != letter:
                if  self.player_guess[index] in self.word_of_the_day and answer_letter_count[self.player_guess[index]] > 0:
                    self.missplaced_letter_indices.append(index)
                    answer_letter_count[self.player_guess[index]] -= 1
                else:
                    self.incorrect_letter_indices.append(index)

    def is_match(self):
        return len(self.correct_letter_indices) == 5

@dataclass
class Wordle:
    word_picker: WordPicker
    word_of_the_day: str = ""
    turns: list[WordleTurn] = field(default_factory=list)

    def __post_init__(self) -> None:
        self.word_of_the_day = self.word_picker.get_word_of_the_day()

    def __last_turn(self) -> WordleTurn:
        return self.turns[-1]

    def get_game_status(self) -> GameStatus:
        if len(self.turns) == 0:
            return GameStatus.NEW
        if self.__last_turn().is_match():
            return GameStatus.WIN
        if len(self.turns) <= 5:
            return GameStatus.CONTINUE
        return GameStatus.LOSS

    def guess(self, word: str) -> None:
        self.turns.append(WordleTurn(self.word_of_the_day, word))
