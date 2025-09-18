# Does a digital stream of 1's and 0's like in the matrix

import random, time

# for each column, 
# generate a random # of the length of column
# for each position in column, put a 1 or 0 random

SCREEN_WIDTH = 80
SCREEN_HEIGHT = 22

def main():
    while True:
        screen_grid = init_screen()
        for y in range(SCREEN_WIDTH):
            # Get a random # for the size of column 
            column_size = random.randint(1, SCREEN_HEIGHT)
            column_start = random.randint(0, SCREEN_HEIGHT - column_size)
            column_end = column_start + column_size
            for x in range(column_start, column_end):
                screen_grid[x][y] = str(random.randint(0,1)) + ' '
        for y in range (SCREEN_HEIGHT):
            print()
            for x in range(SCREEN_WIDTH):
                print(screen_grid[y][x], end='')
        time.sleep(0.5)
                                
    
def init_screen():
    return [[' '] * SCREEN_WIDTH for _ in range(SCREEN_HEIGHT)]

if __name__ == "__main__":
    main()