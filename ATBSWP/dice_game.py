# dice game by Wes Leonard

# 2-6 dice randomly thrown and shown in random spots on screen
# user has 30 seconds to guess as many correctly as possible
# Every guess = new dice roll

import random

TILE_EMPTY = 0
TILE_OCCUPIED = 1
DICE_CORNER = '+'
DICE_TOP = '-'
DICE_SIDE = '|'
MAX_COLS = 80
MAX_ROWS = 21

screen_grid = []

def main():
    for x in range(MAX_ROWS):
        screen_grid.append([])
        for y in range(MAX_COLS):
            screen_grid[x].append(TILE_EMPTY)
            
    clear_screen()
            
    # get # of dice to roll
    number_of_dice = random.randint(2, 6)
    dice_total = 0
    dice_corners = []
    
    for i in range(number_of_dice):
        random_num = random.randint(1, 6)
        dice_total += random_num    
        dice_corners.append(get_dice_location())
        update_grid(dice_corners[i])
    dice_corners = sorted(dice_corners)
        
    # we have everything saved in the lists, need to print the dice now
    print(dice_corners)
    
    for row in screen_grid:
        for col in screen_grid:
            print(col)
    
def clear_screen():
    print('\n' * 100)
    
def get_dice_location():
    # finds an unoccoupied spot to print the die
    location_found = False
    while not location_found:
        # get x between 0 and MAX_ROWS - 6
        # get y between 0 and MAX_COLS - 10
        # check a 9x5 area to see if it fits.
        # if so, location_found = True, return location
        x = random.randint(0, MAX_ROWS - 6)
        y = random.randint(0, MAX_COLS - 10)
        if location_good(x, y):
            location_found = True
            return (x, y)
        
def location_good(row, col):
    
    for x in range(row, row + 5):
        for y in range(col, col + 9):
            if screen_grid[x][y] != TILE_EMPTY:
                return False
    return True
        
def print_dice(n, loc):
    #alternate version of 2, 3, or 6
    if random.randint(0,1) == 0 and (n == 2 or n == 3 or n == 6):
        n = f'{n}b'
    
    x, y = loc[0], loc[1]        
    
    # each die is 9x5
    print_string = ''
    print_string += ' ' * y
    print_string += '\n' * x        
    match n:
        case 1: print_string += '''
                      +-------+
                      |       |
                      |   o   |
                      |       |
                      +-------+
                      '''
        
        case 2: print_string += '''
                      +-------+
                      |     o |
                      |       |
                      | o     |
                      +-------+
                      '''
        
        case '2b': print_string += '''
                      +-------+
                      | o     |
                      |       |
                      |     o |
                      +-------+
                      '''
        
        case 3: print_string += '''
                      +-------+
                      |     o |
                      |   o   |
                      | o     |
                      +-------+
                      '''
        
        case '3b': print_string += '''
                      +-------+
                      | o     |
                      |   o   |
                      |     o |
                      +-------+
                      '''
        
        case 4: print_string += '''
                      +-------+
                      | o   o |
                      |       |
                      | o   o |
                      +-------+
                      '''
        
        case 5: print_string += '''
                      +-------+
                      | o   o |
                      |   o   |
                      | o   o |
                      +-------+
                      '''
        
        case 6: print_string += '''
                      +-------+
                      | o o o |
                      |       |
                      | o o o |
                      +-------+
                      '''
                      
        case '6b': print_string += '''
                      +-------+
                      | o   o |
                      | o   o |
                      | o   o |
                      +-------+
                      '''
                      
    print(print_string)
        
def update_grid(loc):
    row, col = loc[0], loc[1]
    row_num = 0
    col_num = 0
    for x in range(row + 5):
        row_num += 1
        for y in range(col + 9):
            if (col_num == 0 and row_num == 0) or (col_num == 8 and row_num == 0) or (col_num == 0 and row_num == 4) or (col_num == 8 and row_num == 4):
                char = DICE_CORNER
            elif col in [0, 4] and row in [1, 2, 3]:
                char = DICE_SIDE
            else:
                char = ' '
            col_num += 1
    
if __name__ == '__main__':
    main()