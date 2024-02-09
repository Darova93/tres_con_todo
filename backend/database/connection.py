from os import environ
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(environ.get("DB_HOST", "localhost:3306"))
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from . import models
    Base.metadata.create_all(bind=engine)
