from os import environ
from database.connection import db_session
from database.models import WordleWord


# try:
#     client.admin.command('ping')
#     print("Successfully connected to MongoDB!")
#     word_collection = client.games.words

#     id = 1
#     with open("palabras_rae_completo.txt", "r", encoding="utf-8", newline="\n") as words_file:
#         for word in words_file:
#             u = WordleWord(word, '')
#             db_session.add(u)
#         db_session.commit()
#     print(f"Exported {id} entries")
# except Exception as e:
#     print(e)

