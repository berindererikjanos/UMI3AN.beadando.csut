#Berinder Erik János UMI3AN Csütörtök 10:00 HB
#EX6
#Write a program that automatically converts English text to Morse code and vice versa.
#Írj egy olyan programot, amely automatikusan átalakítja az angol szöveget Morse-kódra és fordítva.

morze_kod =    {'A': '.- ', 'B': '-... ', 'C': '-.-. ',
    'D': '-.. ', 'E': '. ', 'F': '..-. ',
    'G': '--. ', 'H': '.... ', 'I': '.. ',
    'J': '.--- ', 'K': '-.- ', 'L': '.-.. ',
    'M': '-- ', 'N': '-. ', 'O': '--- ',
    'P': '.--. ', 'Q': '--.- ', 'R': '.-. ',
    'S': '... ', 'T': '- ', 'U': '..- ',
    'V': '...- ', 'W': '.-- ', 'X': '-..- ',
    'Y': '-.-- ', 'Z': '--.. ',

    '0': '----- ', '1': '.---- ', '2': '..--- ',
    '3': '...-- ', '4': '....- ', '5': '..... ',
    '6': '-.... ', '7': '--... ', '8': '---.. ',
    '9': '----. ',

    ' ': '....... '
    }

morze_kod_vissza =    {'.-': 'A', '-...': 'B', '-.-.': 'C',
    '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I',
    '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O',
    '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U',
    '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',

    '-----': '0', '.----': '1', '..---': '2',
    '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8',
    '----.': '9',

    '.......': ' '

    }

def kodol(uzenet):
    uj_uzenet = ""
    for i in range(0,len(uzenet))
        uj_uzenet += morze_kod[uzenet[i]]
    return uj_uzenet

def dekodol(uzenet):
    lista = uzenet.split(" ")
    print(lista)
    uj_uzenet = ""
    for i in range(0,len(lista)-1):
        uj_uzenet+=morze_kod_vissza[lista[i]]
    return uj_uzenet
        

  

  
