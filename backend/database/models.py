from sqlalchemy import Integer, String
from sqlalchemy.orm import mapped_column
from .connection import Base

class User(Base):
    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    external_id = mapped_column(String(200))
    name = mapped_column(String(50))
    email = mapped_column(String(120), unique=True)
    profile_picture = mapped_column(String(200))
    token = mapped_column(String(255))
