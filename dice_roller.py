'''
Dice roller simulator.
Reads in the format 1d6+1
'''

import random, sys

def main():
    while True:
        roll = input("> ")
        if roll.upper()== "Q":
            sys.exit('Goodbye!')
        num_rolls, num_sides = roll.split('d')
        if '+' in num_sides:
            num_sides, bonus = num_sides.split('+')
        elif '-' in num_sides:
            num_sides, bonus = num_sides.split('-')    
        else:
            bonus = 0
        num_rolls = int(num_rolls)
        num_sides = int(num_sides)
        bonus = int(bonus)
        results = roll_dice(num_rolls, num_sides, bonus)
        total = 0
        result_string = "("
        for result in results:
            total += result
            result_string += f"{str(result)}, "
        result_string = result_string[:-2]
        result_string += ")"
        print(f"{total} {result_string}")
        
def roll_dice(rolls, sides, bonus):
    roll_results = []
    for i in range(rolls):
        roll_results.append(random.randint(1, sides))
    if bonus != 0:
        roll_results.append(bonus)
    return roll_results  
    
if __name__ == "__main__":
    main()