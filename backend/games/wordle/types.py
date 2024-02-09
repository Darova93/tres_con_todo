from enum import Enum

class GameStatus(str, Enum):
    CONTINUE = "CONTINUE"
    NEW = "NEW"
    WIN = "WIN"
    LOSS = "LOSS"

class WordPicker:
    def get_word_of_the_day(self) -> str:
        raise NotImplementedError

    def is_word_valid(self, word: str) -> bool:
        raise NotImplementedError
