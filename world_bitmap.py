'''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................

Get a message from the user and display map using the letters from
that message.

Author: Wes Leonard
Email: leonardw@gmail.com
'''
#Logic
'''
- ask user for a message
- initialize bitmap to ascii image above
- go through bitmap char by char and if there is a * write_letter = True (print appropriate letter). 
    if blank write_letter = False (print a space)
if True print (message[len(message) % bitmap character currently on)

simplified: if *, write letter
you can tell which letter by takign the current index % length of message.
'''
def get_message():
    print('Enter a message')
    return input('> ')

def get_message_char(msg, position):
    character_position = position % len(msg) 
    return msg[character_position]

def main():
    bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **     *                    *
....................................................................    
    '''
    message = get_message()
    for line in bitmap.splitlines():
        new_line = ''
        for i, char in enumerate(line):
            if char == "*":
                new_line += get_message_char(message, i)
            elif char == ".":
                new_line += get_message_char(message, i)
            else:
                new_line += " "       
        print(new_line)
if __name__ == '__main__':
    main()