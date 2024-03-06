import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from sqlalchemy.orm import Session
from database.connection import engine, init_db
from database.models import Word, Language

def load_languages(session):
    session.add(Language(language="Español", locale="es_MX"))
    session.commit()

def load_words(session):
    id = 1
    with open("backend/public/palabras_rae.txt", "r", encoding="utf-8", newline="\n") as words_file:
        for name in words_file:
            u = Word(word=name, locale="es_MX")
            session.add(u)
            id += 1
    session.commit()
    return id

try:
    init_db()
    session = Session(engine)
    load_languages(session)
    id = load_words(session)
    print(f"Exported {id} entries")
except Exception as e:
    print(e)

