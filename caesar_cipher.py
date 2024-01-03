# caesar cipher by kenny zhang

import enchant
import os
import random

letters = 'abcdefghijklmnopqrstuvwxyz'

clear = lambda: os.system('cls')

def cipher():
    inp = input('\nenter message: ')
    inp = inp.lower()
    shift = input('\nenter integer amount to shift: ')
    if not shift.isnumeric():
        shift = int(random.randint(1,25))
    result = ''
    for x in inp:
        if not x.isalpha():
            result += x
        else:
            x = int(letters.find(x) + int(shift))
            result += letters[x%26]
    clear()
    print('\ninput:  ', inp)
    print('output: ', result)
    print('shift:  ', shift)
    main()

def decipher():
    d = enchant.Dict("en_US")
    inp = input('\nenter message: ')
    while inp[0] not in letters:
        clear()
        print('invalid input\n')
        inp = input('enter message: ')
    inp = inp.lower()
    clear()
    print('\ninput:  ', inp)
    result = ''
    temp = ''
    boo = False
    for x in range(25):
        for y in inp:
            if not y.isalpha():
                result += y
            else:
                shift = x + 1
                y = int(letters.find(y) - shift)
                if y <= 0:
                    y = 26 - abs(y)
                result += letters[int(y)%26]
                temp = result.split()
        if d.check(temp[0]) == True:
            print('output: ', result)
            print('shift:  ', str(x+1))
            boo = True
            break
        result = ''
    if boo == False:
        print('output:  no output was found; executing bruce force attack\n')
        table = ('shift    output')
        print(table)
        if len(inp) > 6:
            temp = len(inp) + 9
            print('-' * temp)
        else:
            print('-' * len(table))
        for x in range(25):
            for y in inp:
                if not y.isalpha():
                    result += y
                else:
                    shift = x + 1
                    y = int(letters.find(y) - shift)
                    if y <= 0:
                        y = 26 - abs(y)
                    result += letters[int(y)%26]
                    temp = result.split()
            if (x+1) <= 9:
                print(str(x+1), '      ', result)
            else:
                print(str(x+1), '     ', result)
            result = ''
    main()

def cipher_sample():
    clear()
    print('\ninput:   the quick brown fox jumps over the lazy dog.')
    print('output:  wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj.')
    print('shift:   3')
    main()

def decipher_sample():
    clear()
    print('\ninput:   wkh txlfn eurzq ira mxpsv ryhu wkh odcb grj.')
    print('output:  the quick brown fox jumps over the lazy dog.')
    main()

def main():
    menu = '\ncaesar cipher menu'
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
