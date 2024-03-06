import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from os import environ
from database.connection import init_db
from database.models import WordleWord

print(WordleWord())
