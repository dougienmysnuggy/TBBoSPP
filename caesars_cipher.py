# Caesar Cipher
# This module provides functions to encrypt and decrypt text using the Caesar cipher technique.

# Author: Wes Leonard
# Email: leonardw@gmail.com
# Date: 20230-08-08

'''
Logic:

Choose whether to encrypt or decrypt.
- If encrypting, shift each letter forward by a specified number of positions in the alphabet.
- If decrypting, shift each letter backward by the same number of positions.
- Non-alphabetic characters remain unchanged.
Ask for message and shift value.
- If shifts past 25th postion subtract length of alphabet (26) to get correct position.
- If shift is negative, add 26 to get a positive shift value.

Print Message
copy to clipboard
'''

import sys
try:
    import pyperclip
except ImportError:
    pass

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def transform_message(msg, k, m):
    new_message = ''
    for char in msg:
        if char not in SYMBOLS:
            new_message += char #remains unchanged
        else:
            num = SYMBOLS.find(char)
            if m.upper() == 'D': # check for decrypt mode
                num -= k
            else:
                num += k
                
            # to see if we went past A or Z and adjusts accordingly
            if num >= len(SYMBOLS):
                num -= len(SYMBOLS)
            if num < 0:
                num += len(SYMBOLS)
                
            new_message += SYMBOLS[num]
    return new_message

def main():
    mode = ''
    message = ''
    transformed_message = ''
    
    print('Caesar Cipher by Wes Leonard') 
    #make sure they enter "e" or "d" else ask again
    while True:
        while mode.upper() != 'E' and mode.upper() != 'D':
            mode = input('(e)ncrypt or (d)ecrypt? ')
        #Make sure they put in a valid key
        while True:
            key = int(input('Please enter key (0-25): '))
            if key >= 0 and key < len(SYMBOLS):
                break
        message = input('Please enter message (Type: "QUIT" to exit): ')
        message = message.upper()
        if message.upper() == 'QUIT':
            sys.exit()
        transformed_message = transform_message(message, key, mode)
        print(transformed_message)
        #Copy message to clipboard 
        try:
            pyperclip.copy(transformed_message)
            print('Message copied to clipboard...')
        except:
            pass 

if __name__ == '__main__':
    main()