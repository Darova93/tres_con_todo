import sys
sys.path.append('/home/danielalbinoms/Documents/tres_con_todo/backend')

from os import environ
from database.connection import db_session
from database.models import Word

try:
    id = 1
    with open("./palabras_rae.txt", "r", encoding="utf-8", newline="\n") as words_file:
        for name in words_file:
            u = Word(word=name,locale="es_MX")
            db_session.add(u)
            id += 1
        db_session.commit()
    print(f"Exported {id} entries")
except Exception as e:
    print(e)
