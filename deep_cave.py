# prints a never ending cave

''' 

'''

import random, sys, time

MAX_WIDTH = 80

def main():
    # initial values
    left_side = 35
    gap = 20
    right_side = MAX_WIDTH - gap - left_side
    while True:
        try:
            print('#' * left_side + ' ' * gap + '#' * right_side)
            left_side += random.randint(-1, 1)
            gap += random.randint(-1, 1)
            right_side = MAX_WIDTH - left_side - gap
            
            time.sleep(0.5)
        except KeyboardInterrupt:
            print('Program ended.  DEEP CAVE by Wes Leonard')
            sys.exit()
    
if __name__ == '__main__':
    main()