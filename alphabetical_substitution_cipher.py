# alphabetical substitution by kenny zhang

import os

alphabet = 'abcdefghijklmnopqrstuvwxyz'
cipher_alphabet = 'zyxwvutsrqponmlkjihgfedcba'

clear = lambda: os.system('cls')

def substitute_alphabet(text, substitution_key, reverse_substitution_key):
    result = ''
    for current_char in text:
        if current_char.isupper():
            char_index = int(substitution_key.find(current_char.lower()))
            result += reverse_substitution_key[int(char_index)].upper()
        elif current_char.islower():
            char_index = int(substitution_key.find(current_char))
            result += reverse_substitution_key[int(char_index)]
        else:
            result += current_char
    return result

def cipher():
    inp = input('\nenter a message: ')
    clear()
    print('\ninput:  ', inp)
    print('output: ', substitute_alphabet(inp, alphabet, cipher_alphabet))
    main()

def decipher():
    inp = input('\nenter a message: ')
    clear()
    print('\ninput:  ', inp)
    print('output: ', substitute_alphabet(inp, cipher_alphabet, alphabet))
    main()    

def cipher_sample():
    clear()
    print('\ninput:   The quick brown fox jumps over the lazy dog.')
    print('output:  Gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt.')
    main()

def decipher_sample():
    clear()
    print('\ninput:   Gsv jfrxp yildm ulc qfnkh levi gsv ozab wlt.')
    print('output:  The quick brown fox jumps over the lazy dog.')
    main()


def main():
    menu = '\nalphabetical substitution menu'
    print(menu)
    print('-'*len(menu))
    print('[1] cipher\n[2] decipher\n[3] cipher sample\n[4] decipher sample\n[5] quit')
    option = input('\nenter a menu option and press ENTER: ')
    if option == '1':
        cipher()
    elif option == '2':
        decipher()
    elif option == '3':
        cipher_sample()
    elif option == '4':
        decipher_sample()
    elif option == '5':
        quit()
    else:
        clear()
        print('\ninvalid input')
        main()

if __name__ == "__main__":   
    main()
