import random
import re
from unicodedata import normalize


def read():
    list_words = []
    with open("./archivos/data.txt", 'r', encoding='utf-8') as f:
        for i in f:
            list_words.append(i)
    #enumacion = list(enumerate(list_words))
    int_rdm = random.randint(0, len(list_words))
    word = ""
    for i, words in enumerate(list_words):
        if i == int_rdm:
            word = (words.replace("\n",""))
    
    # -> NFD y eliminar diacríticos
#####fuente https://es.stackoverflow.com/questions/135707/c%c3%b3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l/135736#135736
    word = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", word), 0, re.I    )

    # -> NFC
    word = normalize( 'NFC', word)
#####fuente https://es.stackoverflow.com/questions/135707/c%c3%b3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l/135736#135736
 
    word = word.upper()
    
    return word



def run():
    choosen_word = read()
    print(choosen_word)
    #letter_choosen = "i"
    letters_in_word = list(enumerate(choosen_word))
    #print(letters_in_word)
    #position_letters = [i for i, letter in letters_in_word if letter == letter_choosen.upper() ]
    #print(position_letters)

    encoding = ["_" for i in range(0, len(choosen_word))]
    print(' '.join(encoding))
    count = 0
    while count < 10:
        letter_choosen = input("Ingresa una letra: ")
        
        for n, i in letters_in_word:
            if i == letter_choosen.upper():
                encoding[n] = letter_choosen.upper()
        print(' '.join(encoding))
        count = count + 1

if __name__ == '__main__':
    run()