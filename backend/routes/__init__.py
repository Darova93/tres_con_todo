from . import wordle_api
from . import hangman_api
from . import auth

__MODULES = [
    wordle_api, hangman_api, auth
]

ROUTES = [m.app_route for m in __MODULES]
