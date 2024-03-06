from sqlalchemy import Column, Integer, String, Date, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .connection import Base

class User(Base):
    __tablename__ = "user"
    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name : Mapped[str] = mapped_column(String(50))
    email : Mapped[str] = mapped_column(String(120), unique=True)


class Language(Base):
    __tablename__ = "language"

    language : Mapped[str] = mapped_column(String(20))
    locale : Mapped[str] = mapped_column(String(10), primary_key=True)

class Word(Base):
    __tablename__ = "word"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    word : Mapped[str] = mapped_column(String(50))
    locale : Mapped[str] = relationship(back_populates="language")
    can_be_word_of_the_day : Mapped[bool] = mapped_column(Boolean)

class WordOfTheDay(Base):
    __tablename__ = "word_of_the_day"

    id : Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    word_id : Mapped[int] = relationship(back_populates="word")
    date : Mapped[Date] = mapped_column(Date, unique=True)

