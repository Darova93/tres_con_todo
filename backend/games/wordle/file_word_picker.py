from datetime import datetime
from games.wordle.types import WordPicker

class StartingDate:
    startingDate = None
    def __new__(cls, year, month, day):
        if cls.startingDate is None:
            cls.startingDate = super(StartingDate, cls).__new__(cls)
            cls.year = year
            cls.month = month
            cls.day = day
            cls.timestamp = cls.startingDate.get_timestamp()
        return cls.startingDate

    def get_timestamp(self) -> int:
        startingDateTimestamp = datetime(self.year,self.month,self.day).timestamp()
        return int(startingDateTimestamp)

def get_days_since_starting_date(starting_date_timestamp):
    seconds_in_a_day = 60*60*24
    daysSinceStartingDate = ((int(datetime.now().timestamp()) - starting_date_timestamp)//(seconds_in_a_day)) + 1
    return daysSinceStartingDate

class FileWordPicker(WordPicker):
    valid_word_list: list[str] = []
    file_name: str = "./public/palabras_rae.txt"

    def __init__(self):
        with open(self.file_name, "r", newline="\n", encoding="utf-8") as file:
            for word in file:
                self.valid_word_list.append(word.replace("\n", "").upper())

    def get_word_of_the_day(self) -> str:
        starting_date = StartingDate(2024,1,1)
        todaysAnswer = self.valid_word_list[get_days_since_starting_date(starting_date.get_timestamp())]
        return todaysAnswer
