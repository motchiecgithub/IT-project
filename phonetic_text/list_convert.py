# The program that take a word, convert the word into a list of letter group or phonetic value
from search import *
def list_convert(word):
    # create a list of letter group
    word = word.lower()
    word_list = []
    
    #split letters into groups e.g dearest = ['d', 'ea', 'r', 'e', 's', 't']
    i = 0
    while i < len(word):
        # convert letters into groups
        if (i+1) < len(word):
            if word[i] + word[i+1] in ['ae', 'ai', 'ay', 'ea', 'ee', 'ei', 'ey', 'ie', 'oa', 'oe', 'oi', 'oo', 'ou', 'oy', 'ue', 'ui']:
                word_list.append(word[i] + word[i+1])
                i += 2
            else:
                word_list.append(word[i])
                i += 1
        else:
            word_list.append(word[i])
            i += 1
    
    return word_list


def phonetic_translate_letter(word, letters, language):
    
    # the recived word is in /ˈæpəɫ/ format, remove the / from the word
    word = word.replace("/", "")

    # remove the ' from the word
    word = word.replace("ˈ", "")

    # split each letter in word to a list
    word_list = []
    for letter in word:
        word_list.append(letter)
    
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
            
    