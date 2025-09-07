# Twttr
# Wes Leonard
# 2025-08-21 #updated
import sys

def main():
    try:
        user_input = input('Input: ')
    except Exception:
        sys.exit('Invalid input')
        
    print(shorten(user_input))

def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    no_vowels = ''
    for c in word:
        if c.lower() not in vowels:
            no_vowels += c
    return no_vowels

if __name__ == '__main__':
    main()