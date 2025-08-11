#! python3

'''
Author: Wes Leonard
date: 2025-08-10

This program gets a month and year from the user and prints out the
appropriate monthly calendar

Example:

                            December 2029 (centered)
...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..
+----------+----------+----------+----------+----------+----------+----------+
|25        |26        |27        |28        |29        |30        | 1        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 2        | 3        | 4        | 5        | 6        | 7        | 8        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
| 9        |10        |11        |12        |13        |14        |15        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|16        |17        |18        |19        |20        |21        |22        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|23        |24        |25        |26        |27        |28        |29        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+
|30        |31        | 1        | 2        | 3        | 4        | 5        |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
|          |          |          |          |          |          |          |
+----------+----------+----------+----------+----------+----------+----------+

Logic:
- Get Month from user
- Get Year from user

'''
import datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November' 'December']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']

def print_divider_line():
    print('+----------+----------+----------+----------+----------+----------+----------+')
    
def print_days_of_week():
    print('...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..')
    
def print_date_row(dates):
    print(f'|{str(dates[0]).rjust(2)}        |{str(dates[1]).rjust(2)}        |{str(dates[2]).rjust(2)}        |{str(dates[3]).rjust(2)}        |' +
          f'{str(dates[4]).rjust(2)}        |{str(dates[5]).rjust(2)}        |{str(dates[6]).rjust(2)}        |')
    
def print_verticle_dividers():
    print('|          |          |          |          |          |          |          |')
    
def build_date_list(d, date_num):
    # this function returns a list where
    # sunday = d[0] ... saturday = d[6]
        
    day_of_week = datetime.date.weekday(d)
    
    days_list = {'Monday' : '', 'Tuesday': '', 'Wednesday' : '', 'Thursday' : '',
                 'Friday' : '', 'Saturday' : '', 'Sunday' : ''}
    
    for k, v in days_list.items():
        print(k + ' ' + v)
                    
    return days_list

def main():
    
    calendar = '' #going to build this into a huge string
    
    #get month
    while True:
        month = input('Enter month (1-12): ')
        month = int(month)
        if month >= 1 and month <= 12:
            break
        
    #get year
    while True:
        year = input('Enter the year: ')
        year = int(year)
        if year >= 0 and year <= 9999:
            break
        
    # Determine which day of week
    working_date = datetime.date(year, month, 1)
      
    # Print Header and calendar outline
    header = MONTHS[month - 1] + ' ' + str(year)
    print(header.center(78))
    print_days_of_week()
    
    # Need logic to build the date list
    date_list = build_date_list(working_date, 1)
    
    print_divider_line()
    for i in range(6): # probably need to make this a variable for months that use less rows
        print_date_row(date_list)
        for i in range(3):
            print_verticle_dividers()
        print_divider_line()
            
if __name__ == "__main__":
    main()