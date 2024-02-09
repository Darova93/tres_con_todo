import pytest

from games.wordle.wordle import WordleTurn

@pytest.mark.parametrize("player_guess, correct_word, expected_correct_letter_indices, expected_missplaced_letter_indices, expected_wrong_letter_indices",
                         [('avara', 'maria', [4], [0,3], [1,2]),
                          ('Burro', 'perro', [2,3,4], [], [0,1]),
                          ('HoYoS', 'huelo', [0], [1], [2,3,4]),
                          ('juego', 'juego', [0,1,2,3,4], [], [])])

def test_answer(player_guess: str, correct_word: str, expected_correct_letter_indices: list[int], expected_missplaced_letter_indices: list[int], expected_wrong_letter_indices: list[int]):
    wordle_turn = WordleTurn(correct_word, player_guess)
    assert(wordle_turn.correct_letter_indices == expected_correct_letter_indices)
    assert(wordle_turn.missplaced_letter_indices == expected_missplaced_letter_indices)
    assert(wordle_turn.incorrect_letter_indices == expected_wrong_letter_indices)
