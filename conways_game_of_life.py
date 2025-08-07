# Conway's Game of Life implementation in Python

# Author: Wes Leonard
# Email: leonardw@gmail.com

import random, copy, time

WIDTH = 60
HEIGHT = 20

# build cells
next_cells = []
for x in range(WIDTH):
    column = []
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append('#')
        else:
            column.append(' ')
    next_cells.append(column)

# Main Loop
while True:
    
    print ('\n\n\n\n\n') # Separate the steps
    current_cells = copy.deepcopy(next_cells)
        
    # print the cells
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(current_cells[x][y], end='')
        print()
    
    # Calculte for next_cells
    for x in range(WIDTH):
        for y in range(HEIGHT):
            #get the coordinates of the neighbors
            left_coord = (x - 1) % WIDTH
            right_coord = (x + 1) % WIDTH
            above_coord = (y - 1) % HEIGHT
            below_coord = (y + 1) % HEIGHT
            
            # count the neighbors
            num_neighbors = 0
            if current_cells[left_coord][above_coord] == "#": #Top Left Neighbor
                num_neighbors += 1
            if current_cells[x][above_coord] == "#": #Top Neighbor
                num_neighbors += 1    
            if current_cells[right_coord][above_coord] == "#": #Top Right Neighbor
                num_neighbors += 1
            if current_cells[left_coord][y] == "#": #Left Neighbor
                num_neighbors += 1
            if current_cells[right_coord][y] == "#": #Right Neighbor
                num_neighbors += 1
            if current_cells[left_coord][below_coord] == "#": #Bottom Left Neighbor
                num_neighbors += 1
            if current_cells[x][below_coord] == "#": #Bottom Neighbor
                num_neighbors += 1
            if current_cells[right_coord][below_coord] == "#": #Bottom Left Neighbor
                num_neighbors += 1
            
                
            # set new cells based on the rules
            
            #living cells w 2-3 neighbors stay alive
            if current_cells[x][y] == '#' and (num_neighbors == 2 or num_neighbors == 3):
                next_cells[x][y] = '#'
            elif current_cells[x][y] == ' ' and num_neighbors == 3: #blank with 3 neighbors comes alive
                next_cells[x][y] = '#'
            else: #everything else is dead
                next_cells[x][y] = ' '
                
    time.sleep(1)