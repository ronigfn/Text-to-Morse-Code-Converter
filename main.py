# import statments for sound
import pygame
import time

# alphabet to morse conversion dictionary
alpha_to_morse = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---',
'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..', '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....',
'6':'-....', '7':'--...', '8':'---..', '9':'----.', '0':'-----', ' ':'/'}

# list of forbiden characters
special_char = ['~','!','@','#','$','%','^','&','*','(',')','-','=','_','+','[',']',':',"'",'"',';','|','\\',',','.','?','/','<','>']

# time signatures
ONE_UNIT = 0.12
THREE_UNITS = 3*ONE_UNIT
SEVEN_UNITS = 7*ONE_UNIT
PATH = "morse_sound_files/"


# forbiden char check function
def check_char(string):
    for char in string:
        if char in special_char:
            return True



# make the program run infinantly
run=True
while run:
    # ask the user for a string and convert it to lower case
    user_input = str(input('Please enter your sentence with only letters and numbers: ')).lower()

    # check for forbiden characters
    if check_char(user_input):
        print('Theres a forbiden character in you string. please try again.')
    else:
    # convert to morse
        converted_string = ''
        for char in user_input:
            morse_char = alpha_to_morse[char]
            converted_string = converted_string + morse_char + ' '
        print(f'Morse Code: {converted_string}')
        
        # initiate py game for sound functionality
        pygame.init()

        # parse through the converted string and play the sounds according to Morse Code rules
        for mor_char in converted_string:
            if mor_char == '/':
                time.sleep(SEVEN_UNITS)
            elif mor_char == ' ':
                time.sleep(THREE_UNITS)
            
            else:
                pygame.mixer.music.load(PATH + mor_char.upper() + '.ogg')
                pygame.mixer.music.play()
                time.sleep(ONE_UNIT)
                
