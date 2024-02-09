from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .connection import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)


class Language(Base):
    __tablename__ = "language"

    id = Column(Integer, primary_key=True)
    locale = Column(String(10), unique=True)
    name = Column(String(20))


class WordleWord(Base):
    __tablename__ = "wordle_word"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    word: Mapped[str] = mapped_column(String(50), unique=True)
    definition: Mapped[str] = mapped_column(String(500), unique=True)
    language: Mapped[Language] = relationship(back_populates="language")
