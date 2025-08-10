# This program contains a function that reads
# a dictionary of chess pieces and determines
# if this is a valid chessboard.

# Author: Wes Leonard
# Email: leonardw@gmail.com
# Date: 2025-08-09

#chess_board = {'a1' : ' ', 'b1' : ' ', 'c1' : ' ', 'd1' : ' ', 'e1' : ' ', 'f1' : ' ', 'g1' : ' ', 'h1' : ' '}
#chess_board = {}

'''
1 black king
1 white king
16 pieces max for each player
8 pawns max
all pieces must be on a valid space from 1a to 8h
'''

def is_valid_chessboard(board):
    
    VALID_ROWS = [1,2,3,4,5,6,7,8]
    VALID_COLS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    # create valid spaces seems easier than typing it out
    
    #check for both kings
    if 'bking' not in board.values() or 'wking' not in board.values():
        return False
    
    # count pawns and total pieces for each player 
    white_pawn_count = 0
    black_pawn_count = 0    
    white_piece_count = 0
    black_piece_count = 0
    for space in board.values():
        if space == 'wpawn':
            white_pawn_count += 1
            white_piece_count += 1
        elif space == 'bpawn':
            black_pawn_count += 1
            black_piece_count += 1
        elif space != ' ':
            if space[0] == 'b':
                black_piece_count += 1
            else:
                white_piece_count += 1
    if white_pawn_count > 8 or black_pawn_count > 8:
        return False
    
    if black_piece_count > 16 or white_piece_count > 16:
        return False
    
    # see if each piece is in a valid spot
    for space in board.keys():
        if int(space[0]) not in VALID_ROWS:
            return False
        if space[1] not in VALID_COLS:
            return False
            
    return True # felt like i needed a marker, might delete later

def main():
    chess_board = {'1a' : 'bking', '3h' : 'wking'}
    print (is_valid_chessboard(chess_board))

if __name__ == '__main__':
    main()