from enum import Enum

class GameStatus(str, Enum):
    CONTINUE = "CONTINUE"
    NEW = "NEW"
    WIN = "WIN"
    LOSS = "LOSS"

class WordPicker:
    def get_word_of_the_day(self):
        raise NotImplementedError
