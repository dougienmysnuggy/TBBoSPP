# Brute force to hack caeser_cipher encryption
# Author: Wes Leonard
# Email: leonardw@gmail.com
# Date: 2025-08-09

import sys

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def decrypt_message(msg, k):
    new_message = ''
    for char in msg:
        if char in SYMBOLS:
            # decrypt based on k
            num = SYMBOLS.find(char)
            num += k
            if num > len(SYMBOLS) - 1:
                num -= len(SYMBOLS)
            new_message += SYMBOLS[num]
        else:
            new_message += char
    print(new_message)
    return new_message

def main():    
    message = input('Enter message to decrypt: ')
    for i in range(len(SYMBOLS)):
        transformed_message = decrypt_message(message, i)
        print(transformed_message)

if __name__ == '__main__':
    main()