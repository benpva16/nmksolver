# read_board.py
# Author: benpva16
# Date Created: 2015-12-23
# Purpose: read_board.py returns a list containing the board located at the
#     filepath passed in

def read_board(filepath_in):
    # print(filepath_in)
    board = []
    
    with open(filepath_in) as input_file:
        for line in input_file:
            board.append(line.strip('\n'))

    return board