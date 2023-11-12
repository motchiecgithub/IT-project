# The program that take a word, convert the word into a list of letter group or phonetic value
from search import *
def list_convert(word, language):
    # create a list of letter group
    word = word.lower()
    letters = []

    # convert by language type
    if language == "en_US" or language == "en_UK":
        letters = list_convert_en(word)
    
    if language == "zh_hans":
        letters = list_convert_zh(word)
    
    return letters

# convert en word to a list of letter group
def list_convert_en(word):   
    #split letters into groups
    letters= []
    i = 0
    while i < len(word):
        # convert letters into groups
        if (i+1) < len(word):
            if word[i] + word[i+1] in ['ae', 'ai', 'ay', 'ea', 'ee', 'ei', 'ey', 'ie', 'oa', 'oe', 'oi', 'oo', 'ou', 'oy', 'ue', 'ui']:
                letters.append(word[i] + word[i+1])
                i += 2
            else:
                letters.append(word[i])
                i += 1
        else:
            letters.append(word[i])
            i += 1
    
    return letters   

# convert zh word to a list of letter group
def list_convert_zh(word):
    # split letters into groups
    letters = []
    i = 0
    while i < len(word):
        letters.append(word[i])
        i += 1

    return letters
    
# translate a word to a list of letter group
def phonetic_translate_letter(word, letters, language):
    
    # translate by language type
    if language == "en_US" or language == "en_UK":
        # clean format
        word = word.replace("/", "")
        word = word.replace("ˈ", "")

        # split letters in word into a list  
        word_list = []
        for letter in word:
            word_list.append(letter)   

        lis = translate_letter_en(word_list, letters)
    
    elif language == "zh_hans":
        lis = translate_letter_zh(word, letters)
    
    return lis

# translate en word to a list of letter group
def translate_letter_en(word_list, letters):
    lis = []
    i = 0
    while i < len(word_list):
        if i-1 >= 0 and letters[i] == letters[i-1]:
            lis.append([letters[i], word_list[i-1]])
            i += 1
        else:
            lis.append([letters[i], word_list[i]])
            i += 1

    return lis
# translate zh word to a list of letter group
def translate_letter_zh(word_list, letters):
    lis = []
    i = 0
    while i < len(letters):
        word_list[i] = word_list[i].replace("/", "")
        lis.append([letters[i], word_list[i]])
        i += 1

    return lis         
    