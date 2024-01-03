# a1z26 cipher by kenny zhang

import os

letters = 'abcdefghijklmnopqrstuvwxyz'

clear = lambda: os.system('cls')

def cipher():
    inp = input('\nenter a message: ')
    while inp[0] not in letters:
        clear()
        print('invalid input')
        inp = input('\nenter a message: ')
    inp = inp.lower()
    inp = inp.replace(' ','')
    clear()
    print('\ninput:  ', inp)
    result = ''
    for x in inp:
        result += str(letters.find(x) + 1)
        result += ' '
    print('output: ', result)
    main()

def decipher():
    inp = input('\nenter a message: ')
    result = ''
    for x in inp.split(' '):
        if not x.isdigit():
            continue
            main()
        else:
            try:
                result += chr(int(x) + 96)
            except (OverflowError, ValueError):
                continue
    clear()
    print('\ninput:  ', inp)
    print('output: ', result)
    main()    


def cipher_sample():
    clear()
    print('\ninput:   The quick brown fox jumps over the lazy dog.')
    print('output:  20 8 5 17 21 9 3 11 2 18 15 23 14 6 15 24 10 21 13 16 19 15 22 5 18 20 8 5 12 1 26 25 4 15 7')
    main()

def decipher_sample():
    clear()
    print('\ninput:   20 8 5 17 21 9 3 11 2 18 15 23 14 6 15 24 10 21 13 16 19 15 22 5 18 20 8 5 12 1 26 25 4 15 7')
    print('output:  thequickbrownfoxjumpsoverthelazydog')
    main()

def main():
    menu = '\na1z26 cipher menu'
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
