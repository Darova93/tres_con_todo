import unicodedata


def clean_special_characters(word: str) -> str:
    return unicodedata.normalize('NFD', word).encode('ascii', 'ignore').decode("utf-8")
