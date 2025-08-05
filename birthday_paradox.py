# Birthday Paradox

'''
This program will run a simulation 100,000 times based
on the user's input.

The program will ask how many birthdays it should generate (1-100)
It will generate that many birthdays and count the duplicates.
This will give us a percentage of how many people have the same
birthday in a group of X members.
'''

import random, datetime

def get_num_birthdays():
    return input('Generate how many birthdays? >')

def generate_random_birthday():
    new_year = datetime.date(2001, 1, 1)
    random_number_of_days = datetime.timedelta(random.randint(0, 364))
    birthday = new_year + random_number_of_days
    return birthday

def run_simulation(num_birthdays): 
    birthday_list = []
    for i in range(int(num_birthdays)):
        birthday = generate_random_birthday()
        birthday_list.append(birthday)
    return birthday_list

def check_for_matches(birthday_list):
    if len(birthday_list) != len(set(birthday_list)):
        return True
    else:
        return False

def update_progress(n):
    if n % 10000 == 0:
        print ('{} Simulations Ran...'.format(n))
        
def display_results(matches):
    #Calculate percentage
    percent_matched = (matches / 100000) * 100
    percent = "{:.2f}".format(percent_matched)
    print('\n100000 Simulations total')
    print('{} with matching birthdays'.format(matches))
    print('{} had at least 2 people with the same birthday'.format(percent))

def main():
    number_of_birthdays = input('Enter # of people in the room (1 - 100): ') 
    number_of_matches = 0   
    for i in range(100001):
        birthdays = run_simulation(number_of_birthdays)
        if check_for_matches(birthdays):
            number_of_matches += 1
        update_progress(i)
    display_results(number_of_matches)
        
if __name__ == '__main__':
    main()