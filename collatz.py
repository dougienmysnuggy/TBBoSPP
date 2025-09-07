# collatz sequence

def main():
    running = True
    while running:
        # get user #
        num = input('> ')
        if num.upper() == 'QUIT':
            running = False
            continue
        if not num.isdecimal():
            print('Invalid input. Please enter a number')
            continue
        else:
            num = int(num)
        print(num, end='', flush=True)
        while num != 1:
            if is_even(num):
                num //= 2 
            else:
                num = num * 3 + 1
            print(f', {num}', end='', flush=True)
        print()
        
def is_even(n):
    return n % 2 == 0
            
if __name__ == '__main__':
    main()