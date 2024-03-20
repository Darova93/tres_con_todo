from sqlalchemy import Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .connection import Base

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    external_id = mapped_column(String(200))
    name = mapped_column(String(50))
    email = mapped_column(String(120), unique=True)
    profile_picture = mapped_column(String(200))
    token = mapped_column(String(255))

class Language(Base):
    __tablename__ = "language"

    id = mapped_column(Integer, primary_key=True)
    locale = mapped_column(String(10), unique=True)
    name = mapped_column(String(20))

class WordleWord(Base):
    __tablename__ = "wordle_word"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    word: Mapped[str] = mapped_column(String(50), unique=True)
    definition: Mapped[str] = mapped_column(String(500), unique=True)
    language: Mapped[Language] = relationship(back_populates="language")
