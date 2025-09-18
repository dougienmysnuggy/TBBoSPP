import sevseg, sys, time
from datetime import datetime

def main():
    clear_screen()
    
    while True:
        current_datetime = datetime.now()
        try:
            hours = current_datetime.hour
            minutes = current_datetime.minute
            seconds = current_datetime.second
            top_row, middle_row, bottom_row = big_digits(hours, minutes, seconds)
            print(top_row)
            print(middle_row)
            print(bottom_row)
            print('\nControl + C to Quit')
            time.sleep(1)
            clear_screen()
        except KeyboardInterrupt:
            sys.exit('Clock canceled')
    
def big_digits(hours, minutes, seconds):
    h_digits = sevseg.getSevSegStr(hours, 2)
    h_top, h_middle, h_bottom = h_digits.splitlines()

    m_digits = sevseg.getSevSegStr(minutes, 2)
    m_top, m_middle, m_bottom = m_digits.splitlines()

    s_digits = sevseg.getSevSegStr(seconds, 2)
    s_top, s_middle, s_bottom = s_digits.splitlines()

    top_row = h_top + '   ' + m_top + '   ' + s_top
    middle_row = h_middle + ' * ' + m_middle + ' * ' + s_middle
    bottom_row = h_bottom + ' * ' + m_bottom + ' * ' + s_bottom
    
    return top_row, middle_row, bottom_row

def clear_screen():
    print('\n' * 100)

if __name__ == '__main__':
    main()