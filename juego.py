import random
import re
from unicodedata import normalize
import os
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

def read(): #Con esta funcion leeremos el archivo y el sistema eligira una palabra al azar
    list_words = [] #Genero una lista vacia
    with open("./archivos/data.txt", 'r', encoding='utf-8') as f: #abro el archivo con sistema unicode y lo asisgno a la variable f
        for i in f: #leo los items (lineas) de mi archivo
            list_words.append(i) #agrego cada palabra del archivo a la lista vacia
    #enumacion = list(enumerate(list_words))
    int_rdm = random.randint(0, len(list_words)) #elijo un numero random
    word = "" #defino la variable word, vacia
    for i, words in enumerate(list_words): #uso enumerate para facilitar la busqueda en la lista
        if i == int_rdm: #asigno el numero random a la variable la iteracion i, de modo que cuando la iteracion sea igual al nmero random, el sistema ingresa en la condicion
            word = (words.replace("\n","")) #asigno la palabra que esta en la iteracion i = al numero random (con replace le saco el salto de linea)
    
    # -> NFD y eliminar diacríticos. Las siguientes lineas de codigo son para eliminar dieresis de las palbras y acentos.
#####fuente https://es.stackoverflow.com/questions/135707/c%c3%b3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l/135736#135736
    word = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", word), 0, re.I    )

    # -> NFC
    word = normalize( 'NFC', word)
#####fuente https://es.stackoverflow.com/questions/135707/c%c3%b3mo-puedo-reemplazar-las-letras-con-tildes-por-las-mismas-sin-tilde-pero-no-l/135736#135736
 
    word = word.upper() 
    
    return word
                                                                                                                                                                                                                           
                                                                                                                                                                                                                                                                           

def ganaste():
    pass
def perdiste():
    pass

def run():
    os.system ("cls") #limpio pantalla
    
    choosen_word = read() #asigno la palabra elegida a la variable nueva
    #print(choosen_word)
    encoding = ["_" for i in range(0, len(choosen_word))] #creo una lista para simular la codificacin de las letras de mis palabras
    error = 0
    print(HANGMANPICS[error])
    print('\n')
    print(' '.join(encoding)) #la muestro
    count = 0 #inicio un contador
    list_letter_choosen = []
    test_list = [x for x in encoding if x == "_"]
    
    while error < 7:
        #primero permito al usuario elegir una letra o arriesgar palabra
        letter_choosen = input("\n\n---OPCIONES---\n1-Puedes ingresar una letra o,\n2-Puedes arriesgar la palabra si ya sabes cual es, para eso ingresa '1'\n3-Si quieres abandonar el juego ingresa '2'\n(elegir letra, 1 o 2):")
        #count = count + 1
            
        #normalizo la letra o palabra escrita
        letter_choosen = re.sub(r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", letter_choosen), 0, re.I    )
        # -> NFC
        letter_choosen = normalize( 'NFC', letter_choosen)        
        list_letter_choosen.append(letter_choosen)
        
        if letter_choosen.isdigit(): #primero analizo si el usuario quiere arriesgar palabra o salir del programa
            if int(letter_choosen) == 1:
                word_win_choosen = input("Ingresa la palabra Ganadora: ")
                if word_win_choosen.upper() == choosen_word:
                    print("Ganaste")
                    puntaje = 10 - error + 5
                    print ("Tu puntuacion es:\n"+ str(puntaje) + " puntos")
                    break
                else:
                    print(HANGMANPICS[6])
                    print("Perdiste\nNo sumas puntos" )
                    break
            elif int(letter_choosen) == 2:
                print("Nos abandonaste maldito\nTienes -1000 puntos. Te odiamos.\nVuelva Pronto")
                break
        
        os.system ("cls") #limpio pantalla

        if len(letter_choosen) == 1: #analizo si paso una o mas letras (no tiene permito pasar mas de una letra a menos que arriegue palabra)
            j = 0
            for n, i in enumerate(choosen_word):                
                if i == letter_choosen.upper():
                    encoding[n] = letter_choosen.upper()
                else:
                    j = j + 1
                if j == len(choosen_word):
                    error = error + 1
                    print(error)
            os.system ("cls") #limpio pantalla
            print(HANGMANPICS[error])   
            print(' '.join(encoding))
            print('\n')
            print(' '.join(list_letter_choosen))
            if error == 6:
                break
           
            test_list = [x for x in encoding if x == "_"]
           
            if test_list == []:
                os.system ("cls")
                print("Ganaste")
                puntaje = 10 - error
                print ("tu puntuacion es:\n"+ str(puntaje) + " puntos")
                break
        else:            
            print("Debes ingresar solo una letra")
            

                  
    if test_list != [] and error == 6:
        print("\n\nTe Moriste.\nLa palabra era " + choosen_word)
    


if __name__ == '__main__':
    run()