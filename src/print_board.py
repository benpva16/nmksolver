# print_board.py
# Author: benpva16
# Date Created: 2015-12-24
# Purpose: prints out the board passed in

def print_board(board):
    files = "  a b c d e f g h  " # left-to-right with one space of padding
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1'] # top-to-bottom
    # first, print the files
    print (files)
    i = 0
    for line in board:
        # print the rank, then the row, then the rank again
        print(ranks[i] + ' ' + " ".join(line) + ' ' + ranks[i])
        i += 1
    # finally, print the files again
    print (files)