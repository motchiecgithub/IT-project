# Phonetic text program
# Take a word passed from user input with the selected language
# Return the phonetic text of the word from corresponding dictionary

def phonetic_translate_word(word, language):
    # convert word to lowercase
    word = word.lower()

    # open the language.txt file
    dic = open("dict/" + language + ".txt", "r", encoding="utf-8")

    # search result indicator
    found = False

    # search the word in the dictionary
    for line in dic:

        # split the line in a list of words
        line = line.split()

        # if the word is in the dictionary
        if word in line:

            # return the phonetic text
            found = True
            return line
    
    # if the word is not in the dictionary
    if not found:
        return "Word Not found, try other search method"
    
def phonetic_translate_words(words, language):
    # convert words to lowercase
    words = words.lower()

    # open the language.txt file
    dic = open("dict/" + language + ".txt", "r", encoding="utf-8")

    # created a empty list to store the phonetic text
    phonetic_text = []

    # search the word in the dictionary
    for word in words:
        for line in dic:  
            # split the line in a list of words
            line = line.split()
    
            # if the word is in the dictionary
            if word in line:
                phonetic_text.append(line)
            else:
                phonetic_text.append(word + " not found")
    return phonetic_text






