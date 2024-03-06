from sqlalchemy import ForeignKey, Integer, String, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from .connection import Base

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(50))
    email = mapped_column(String(120), unique=True)

class Language(Base):
    __tablename__ = "language"

    language = mapped_column(String(20))
    locale = mapped_column(String(10), primary_key=True)

class Word(Base):
    __tablename__ = "word"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    word = mapped_column(String(50))
    locale: Mapped[str] = mapped_column(ForeignKey("language.locale"))
    can_be_word_of_the_day = mapped_column(Boolean)

class WordOfTheDay(Base):
    __tablename__ = "word_of_the_day"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    word_id: Mapped[int] = mapped_column(ForeignKey("word.id"))
    date = mapped_column(Date, unique=True)
