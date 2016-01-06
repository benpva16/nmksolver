# solve_board.py
# Author: benpva16
# Date Created: 2015-12-24
# Purpose: returns a list of the pieces in order of a solution

from Piece import Piece

def dfs(piece, pieces, working_solution):
    piece.seen = True
    working_solution.append(piece)

    # Check if working_solution is valid
    # All pieces are used
    # Last piece in solution is the king
    if len(pieces) == len(working_solution) and working_solution[-1].kind == 'k':
        print("Solution:")
        for p in working_solution:
            p.display_piece()
        return

    candidates = piece.get_capture_candidates(pieces)
    for p in candidates:
        if not p.seen:
            dfs(p, pieces, working_solution)
    piece.seen = False
    del working_solution[-1]

def solve_board(starting_piece, pieces):
    for p in pieces:
        p.seen = False
    starting_piece.seen = True
    working_solution = []
    dfs(starting_piece, pieces, working_solution)