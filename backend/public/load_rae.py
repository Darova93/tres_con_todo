import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from os import environ
from database.connection import db_session, init_db
from database.models import Word

try:
    init_db()
    id = 1
    with open("backend/public/palabras_rae.txt", "r", encoding="utf-8", newline="\n") as words_file:
        for name in words_file:
            print(name)
            u = Word(word=name, locale="es_MX")
            db_session.add(u)
            id += 1
        db_session.commit()
    print(f"Exported {id} entries")
except Exception as e:
    print(e)
