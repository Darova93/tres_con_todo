from wordle import ValidWords

def validateRequest(wordleRequest):
    for turn in range(len(wordleRequest["words"])):
        word = wordleRequest["words"][turn]["word"]
        try:
            if len(word) != 5:
                return None
        except:
            return None
    return wordleRequest

def checkDictionaryListWords(wordleRequest):
    validWords = ValidWords()
    playerWords = []
    for turn in range(len(wordleRequest["words"])):
        if (wordleRequest["words"][turn]["word"]).upper() not in validWords.validWordsList:
            return None
        #playerWords.append(wordleRequest["words"][turn]["word"].upper())
    return wordleRequest

def checkSpecialCaractersInValidWords(words):
    validWords = ValidWords()
    specialLetters = ["Á", "É", "Í", "Ó", "Ú", "Ñ", "Ü"]
    normalLetters = ["A", "E", "I", "O", "U", "N", "U"]
    newWords = list()
    for roundWord in words:
        roundWord.upper()
        newRoundWord = list()
        for letter in range(len(specialLetters)):
            if specialLetters[letter] in validWords.todaysAnswerNoAccentMark:
                indexAnswer = validWords.todaysAnswerNoAccentMark.find(specialLetters[letter])
                if normalLetters[letter] == roundWord[indexAnswer]:
                    newRoundWord = list(roundWord)
                    newRoundWord[indexAnswer] = specialLetters[letter]
                    newRoundWord = "".join(newRoundWord)
        if newRoundWord in validWords.validWordsList:
            newWords.append(newRoundWord)
        else:
            newWords.append(roundWord)
    return newWords
