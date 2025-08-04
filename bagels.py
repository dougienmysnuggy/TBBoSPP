# Bagels program from TBBofSPP
# Author: Wes Leonard
# Email: leonardw@gmail.com

'''
This program will ask the user to guess a number. 
The user will get X amount of attempt to guess the number

Pico = You have a correct digit in the wrong place
Fermi = You have a correct digit in its correct place
Bagels = Your guess has zero correct digits

TODO: error checking

'''

import random, sys
NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    
    secret_number = get_secret_number() # Get the secret number
    
    print('''Bagels - A deductive Logic Game

Instructions: CPU will think of a {}-digit number with no repeat digits
You will have {} maximum attempts to guess the number

Clues:  Pico = One digit is correct but in the wrong position
        Fermi = One digit is correct and in the right position
        Bagels = No digits are correct
        
For example, if the secret number was 248 and your guess was 843, the
clues would be Fermi Pico.
          '''.format(NUM_DIGITS, MAX_GUESSES))
    win = False
    guess_attempt_num = 0
    #Main Game Loop
    while win != True:
        guess_attempt_num += 1
        # Get some user input for guesses
        user_guess = get_user_input()    
        
        # Check the guess against the secret number
        guess_result = check_guess(user_guess, secret_number)
        
        if user_guess == secret_number:
            win = True
            print('YOU WIN!!!')
            sys.exit()
        else:
            win = False
            print(guess_result)
            
        # Check for max guesses
        if guess_attempt_num == MAX_GUESSES:
            print('You''ve used all your guesses! YOU LOSE!')
            sys.exit()
        
  
def get_secret_number():
    # Function that returns a secret number. 
    numbers = list('0123456789')
    random.shuffle(numbers)
    secret_num = ''
    for i in range(NUM_DIGITS):
        secret_num += str(numbers[i])
    return secret_num

def get_user_input():
    # Gets a NUM_DIGITS number from the user
    guess = input('Enter a {}-digit number:  '.format(NUM_DIGITS))
    if len(guess) != NUM_DIGITS:
        print('Enter a {} number!'.format(NUM_DIGITS))
        get_user_input()
    else:
        return guess
    
def check_guess(guess, secret):
    #Check the guess against the secret_number
    # Initialize the results string
    result = ''
    
    for i in range(NUM_DIGITS):
        # Check for Fermi
        if guess[i] == secret[i]:
            result += 'Fermi '
        # Check for Pico
        elif guess[i] in secret:
            result += "Pico "
        # Else don't add anything
        else:
            continue
        
    if result == '':
        return "Bagels"
    else:
        return result
    
if __name__ == '__main__':
    main()