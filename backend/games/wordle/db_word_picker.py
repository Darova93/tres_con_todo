from games.wordle.types import WordPicker
from database.models import WordleWord

class DbWordPicker(WordPicker):
    def get_word_of_the_day(self) -> str:
        return str(WordleWord.query.first().word)

    def is_word_valid(self, word: str) -> bool:
        return True
