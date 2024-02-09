from . import wordle_api
from . import hangman_api

__MODULES = [
    wordle_api, hangman_api
]

ROUTES = [m.app_route for m in __MODULES]
