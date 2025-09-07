# 16 - Diamonds

def main():
    print(diamond(10, True))
    for diamond_size in range(10):
        print(diamond(diamond_size, True))
    
def diamond(n, ornate):
    if ornate:
        return filled_diamond(n)
    line = ''
    spaces = n
    for i in range(n):
        line += (' ' * spaces + '/' + ' ' * (i * 2) + '\\\n')
        spaces -= 1
    spaces = 1
    level = n
    for i in range(n):
        line += (' ' * (spaces) + '\\' + ' ' * ((level - 1) * 2) + '/\n')
        spaces += 1
        level -= 1
    return line

def filled_diamond(n):
    line = ''
    spaces = n
   
    for i in range(n):    
        left_side = '/' + '/' * i
        right_side = '\\' + '\\' * i
        line += (' ' * spaces + left_side + right_side + '\n')
        spaces -= 1
    spaces = 1
    level = n - 1
    for i in range(n):
        left_side = '\\' + '\\' *  level
        right_side = '/' + '/' * level 
        line += (' ' * (spaces) + left_side + right_side + '\n')
        spaces += 1
        level -= 1
    return line

if __name__ == '__main__':
    main()