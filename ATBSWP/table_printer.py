def main():
    table_data = [['apples', 'oranges', 'cherries', 'banana'],
                  ['Alice', 'Bob', 'Carol', 'David'],
                  ['dogs', 'cats', 'goose', 'moose']]
    
    print_table(table_data)

def print_table(t):
    max_col_width = get_col_width(t)
    for x in range(len(t[0])):
        line = ''
        for y in range(len(t)):
            line += t[y][x].rjust(max_col_width) 
        print(line)
        
def get_col_width(td):
    max_width = 0 
    for y in range(len(td)):
        for x in td[y]:
            if len(x) > max_width:
                max_width = len(x)
    return max_width
    
    
if __name__ == "__main__":
    main()