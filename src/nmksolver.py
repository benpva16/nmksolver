# nmksolver.py
# Author: benpva16
# Date Created: 2015-12-23
# Purpose: nmksolver solves No More Kings boards

import os

from Piece import Piece
from parse_args import parse_args
from read_board import read_board
from print_board import print_board
from parse_board import parse_board
from solve_board import solve_board

def main():
    temp = parse_args()
    if temp == (0, 0):
        return
    else:
        board_filename = 'boards' + os.sep + "%s" % temp[0] + '-' + "%s" % temp[1] + '.txt'
    board = read_board(board_filename)
    print_board(board)
    pieces = parse_board(board)

    # Get starting and ending pieces
    # The starting piece is denoted by a capital letter
    starting_piece = next((x for x in pieces if x.kind.isupper()), None)
    if starting_piece is None:
        print("Could not find starting piece!")
        return
    else:
        print("Starting piece:")
        starting_piece.display_piece()

    # The ending piece is the king k
    ending_piece = next((x for x in pieces if x.kind == 'k'), None)
    if ending_piece is None:
        print("Could not find ending piece!")
        return
    else:
        print("Ending piece:")
        ending_piece.display_piece()

    solve_board(starting_piece, pieces)

main()