import random, sys, time

try:
    import bext
except ImportError:
    print('This program requires the bext module!')
    sys.exit()
    
WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUMBER_OF_LOGOS = 5
PAUSE_AMOUNT = 0.1
COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

UP_RIGHT = 'ur'
UP_LEFT = 'ul'
DOWN_RIGHT = 'dr'
DOWN_LEFT = 'dl'
DIRECTIONS = (UP_RIGHT, UP_LEFT, DOWN_RIGHT, DOWN_LEFT)

COLOR = 'color'
X = 'x'
Y = 'y'
DIR = 'direction'

def main():
    bext.clear()
    
    #Generate Logos
    logos = []
    for i in range(NUMBER_OF_LOGOS):
        logos.append({COLOR: random.choice(COLORS),
                      X: random.randint(1, WIDTH - 4),
                      Y: random.randint(1, HEIGHT - 4),
                      DIR: random.choice(DIRECTIONS)})
    
    # Make sure X is even so it can hit corner
    if logos[-1][X] % 2 == 1:
        logos[-1][X] -= 1
        
    corner_bounces = 0
    
    while True: # Main loop
        # Erase the logo's current location
        for logo in logos:
            bext.goto(logo[X], logo[Y])
            print('   ', end = '')
            
            original_direction = logo[DIR]
            
            #See if logo bounces off corners
            if logo[X] == 0 and logo[Y] == 0:
                logo[DIR] = DOWN_RIGHT
                corner_bounces += 1
            elif logo[X] == 0 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_RIGHT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == 0:
                logo[DIR] = DOWN_LEFT
                corner_bounces += 1
            elif logo[X] == WIDTH - 3 and logo[Y] == HEIGHT - 1:
                logo[DIR] = UP_LEFT
                corner_bounces +=1 
            #check left edge
            elif logo[X] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = UP_RIGHT
            elif logo[X] == 0 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = DOWN_RIGHT
            #check right edge
            elif logo[X] == WIDTH - 3 and logo[DIR] == UP_RIGHT:
                logo[DIR] = UP_LEFT
            elif logo[X] == WIDTH - 3 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = DOWN_LEFT
                
            #check top edge
            elif logo[Y] == 0 and logo[DIR] == UP_LEFT:
                logo[DIR] = DOWN_LEFT
            elif logo[Y] == 0 and logo[DIR] == UP_RIGHT:
                logo[DIR] = DOWN_RIGHT
                
            #check bottom edge
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_LEFT:
                logo[DIR] = UP_LEFT
            elif logo[Y] == HEIGHT - 1 and logo[DIR] == DOWN_RIGHT:
                logo[DIR] = UP_RIGHT
                
            # change color when change direction
            if logo[DIR] != original_direction:
                logo[COLOR] = random.choice(COLORS)
            
            # move the logo
            if logo[DIR] == UP_RIGHT:
                logo[X] += 2
                logo[Y] -= 1
            if logo[DIR] == UP_LEFT:
                logo[X] -= 2
                logo[Y] -= 1
            if logo[DIR] == DOWN_RIGHT:
                logo[X] += 2
                logo[Y] += 1
            if logo[DIR] == DOWN_LEFT:
                logo[X] -= 2
                logo[Y] += 1
                
            bext.goto(5, 0)
            bext.fg('white')
            print('Corner Bounces: ', corner_bounces, end = '')
            
            # redraw logos at new location
            for logo in logos:
                bext.goto(logo[X], logo[Y])
                bext.fg(logo[COLOR])
                print('DVD', end='')
                
            bext.goto(0, 0)
            
            sys.stdout.flush()
            time.sleep(PAUSE_AMOUNT)
            
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print()
        print('Bouncing DVD Logo Program')
        sys.exit()
        