# Birthday Paradox

'''
This program will run a simulation 100,000 times based
on the user's input.

The program will ask how many birthdays it should generate (1-100)
It will generate that many birthdays and count the duplicates.
This will give us a percentage of how many people have the same
birthday in a group of X members.
'''

#Logic
'''
- Get a number between 1-100 from user
- generate that many random birthdays
    - new list
    - set date to 1/1/2001
    - get a random # days between 1-365
    - add that random # to the 1/1/2001 date
    - append that date to the list.
    - year is irrelevant 
    
- Check to see if any of the birthdays match
    -if they match match = True, else match = False
    - match_count += 1
    - sim_count += 1
    
- Repeat 100K times
    - Create a progress counter
    - if counter % 10K == 0 print a message showing counter
    
- When done display the stats
'''

def get_num_birthdays():
    continue

def run_simulation(): 
    continue

def check_for_matches():
    continue

def update_progress():
    continue

def main():
    
    number_of_birthdays = get_num_birthdays()    
    print('0 Simulations Ran...')
    for i in range(100000):
        run_simulation()
        check_for_matches()
        update_progress()
    
    # create a list of birthdays
    birthday_list = []
    duplicate_counter = 0
    
    
    for i in range(number_of_birthdays):
        birthday = generate_random_birthday()
        birthday_list.append(birthday)
        
        # check birthday list for duplicates
        if len(birthday_list) != len(set(birthday_list)):
            duplicate_counter += 1

        # progress updates
        if i % 10000 == 0:
            print('{} Simulations Ran...'.format(i))
    
if __name__ == '__main__':
    main()