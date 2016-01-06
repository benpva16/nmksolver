# parse_board.py
# Author: benpva16
# Date Created: 2015-12-24
# Purpose: returns list of Pieces on the board

from Piece import Piece

def parse_board(board):
    pieces = []
    row = 0
    col = 0
    for line in board:
        for c in line:
            if c in '.\n ':
                pass
            else:
                pieces.append(Piece(c, row, col))
            col += 1
        row += 1
        col = 0

    return pieces