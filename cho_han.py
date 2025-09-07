# cho-han dice game (odd or even)

import random

def main():
    money = 5000    
    print('''
          Welcome to Cho-Han (Even or Odd)
          2 dice will be swirled in a cup and slammed on the ground
          player chooses cho (even) or han(odd)
          ''')
    
    while True:
        bet = input(f'You have ${money}. How much do you want to bet? (QUIT to exit) ')
        if bet.upper() == 'QUIT':
            break
        else:
            if not bet.isdecimal():
                print('Please enter a valid # or QUIT')
                continue
            bet = float(bet) #needs tighenting up to verify input
            if bet > money:
                print('You don\'t have that much money. Try again.')
                continue
            else:
                money -= bet
        print('''The dealer swirls the cup and you hear the rattle of the dice
              The dealer slams the cup on the ground still covering the
              dic and asks for your play (cho or han).\n\n
              ''')
        valid_play = False
        while not valid_play:
            play = input('Cho (even) or Han (odd)? ')
            if play.upper() in ['CHO', 'EVEN', 'HAN', 'ODD']:
                valid_play = True
            else:
                print('Please enter a valid play. Try again.')
                 
        play = play.upper()
        dice1, dice2 = random.randint(1, 6), random.randint(1, 6)
        show_dice(dice1, dice2)
        
        #check for winner
        if is_even(dice1 + dice2):
            if play == 'CHO' or play == 'EVEN':
                money += bet * 2
                print(f'You win ${bet}! You now have ${money}.')
            else:
                print('You lost. Try again')
        else:
            if play == 'HAN' or play == 'ODD':
                money += bet * 2
                print(f'You win ${bet}! You now have ${money}.')        
            else:
                print('You lost. Try again.')
                
        print()
        
        
def is_even(total):
    return total % 2 == 0
            
def show_dice(d1, d2):
    print('Dice #1 - Dice #2')
    print('-----------------')
    print(f'   {d1}       {d2}')
    
if __name__ == '__main__':
    main()

