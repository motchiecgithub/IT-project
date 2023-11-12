from phonetics import *

# function that take a word and return the soundex
def phonetic_soundex(word):
    # translate to soundex
    soundex_code = soundex(word)
    return soundex_code

# function that take a word and return the metaphone
def phonetic_metaphone(word):
    # translate to metaphone
    metaphone_code = metaphone(word)
    return metaphone_code

def phonetic_soundex_words(words):
    # created a empty list to store the phonetic text
    soundexes = []

    # translate to soundex
    for word in words:
        soundexes.append(soundex(word))
    return soundexes

def metaphone_words(words):
    # created a empty list to store the phonetic text
    metaphones = []

    # translate to metaphone
    for word in words:
        metaphones.append(metaphone(word))
    return metaphones



        



