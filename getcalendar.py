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
import datetime, os

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November' 'December']

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']

def print_divider_line():
    return '+----------+----------+----------+----------+----------+----------+----------+\n'
    
def print_days_of_week():
    return '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
   
def print_verticle_dividers():
    return '|          |          |          |          |          |          |          |\n'
    
def main():   
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

    working_date = datetime.date(year, month, 1)
         
    calendar = ''
    # Print Header and calendar outline
    header = MONTHS[month - 1] + ' ' + str(year)
    calendar += header.center(78)
    calendar += '\n\n'
    calendar += print_days_of_week()
    calendar += print_divider_line()

    # loop this until we are done
    while True:    
        date_line = '' #string to build line
        while datetime.date.weekday(working_date) != 6: #backtrack to Sunday
            working_date -= datetime.timedelta(days=1) # go back 1 day
        for i in range(7):
            day_num = str(working_date.day).rjust(2)
            date_line += '|' + day_num + '        '
            working_date += datetime.timedelta(days=1)
        calendar += date_line    
        calendar += '|\n'
        for i in range(3):
            calendar += print_verticle_dividers()
        calendar += print_divider_line()
        if working_date.month != month:
            break    

    print (calendar)
    
    # save calendar as text file
    calendar_file_name = 'calender_{}_{}.txt'.format(year, month)
    with open(calendar_file_name, 'w') as file_obj:
        file_obj.write(calendar)
        
    print('Calendar saved as file: {}'.format(calendar_file_name))
            
if __name__ == "__main__":
    main()