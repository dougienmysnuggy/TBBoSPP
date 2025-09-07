# Carrot in a box.

'''
    create 2 boxes
    put a carrot in a random box but don't show yet
    randomly assign a box to each player
    tell player 2 to close eyes
    show player 1 contents of box.
    clear screen
    ask player2 if they want to switch
    if yes, switch boxes
    reveal carrot and display winner
'''

import random, time

def main():
    # get players' names
    player1 = get_names(1)
    player2 = get_names(2)
    players = []
    players.append(player1)
    players.append(player2)
    random.shuffle(players)
    
    # let's place the carrot
    boxes = ['c', '']
    random.shuffle(boxes)
    
    # initalize the boxes and start game
    initialize_game(players)
    
    # show player 1 what's in the box
    show_box_contents(players, boxes)
    
        
def get_names(p):
    return input(f'Player {p} name: ')    

def initialize_game(p):
    print(f'''HERE ARE YOUR BOXES:
          
           _________       _________
          /        /|     /        /| 
         +--------+ |    +--------+ |
         |  Red   | |    |  Gold  | |
         |  Box   | /    |  Box   | /
         +--------+/     +--------+/
          {p[0]}           {p[1]}
        
          ''')
    print()
    print(f'{p[0]} you have the red box in front of you')
    print(f'{p[1]} you have the gold box in front of you')
    input('Press Enter to continue....')    
    print('\n' * 100)
    input(f'When {p[1]} has closed their eyes, press enter...')
    print(f'{p[0]} here is what\'s inside of your box...')
    
def show_box_contents(p, b):
    '''
    need to determine which box has the carrot and print accordingly
    '''
    if b[0] == 'c': #carrot in first box
       print(f''' 
              VV
              VV      
              VV
           ___||___        _________
          /   ||   /|     /        /| 
         +--------+ |    +--------+ |
         |  Red   | |    |  Gold  | |
         |  Box   | /    |  Box   | /
         +--------+/     +--------+/
          (Carrot!)
          {p[0]}           {p[1]}
             ''')
    else:
        print(f''' 
                              VV
                              VV
                              VV
           _________       ___||____
          /        /|     /   ||   /| 
         +--------+ |    +--------+ |
         |  Red   | |    |  Gold  | |
         |  Box   | /    |  Box   | /
         +--------+/     +--------+/
                          (Carrot!)
          {p[0]}           {p[1]}
             ''')
        
    input('Press Enter to continue....')
        
    
if __name__ == "__main__":
    main()