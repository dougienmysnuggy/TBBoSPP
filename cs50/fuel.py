def main():
    fraction = input('Fraction: ')
    percent = convert(fraction)
    print(gauge(percent))

def convert(fraction):
    x, y = fraction.split('/')
    while True:
        try:
            if int(x) <= int(y):
                if int(x) >= 0 and int(y) >= 0:
                    percent = int(x) / int(y) * 100
                    return percent
        except ValueError:
            pass

        except ZeroDivisionError:
            pass

def gauge(percentage):
    percentage = round(percentage)
    if percentage <= 1:
        return('E')
    elif percentage >= 99:
        return('F')
    else:
        return(str(percentage) + '%')

if __name__ == "__main__":
    main()