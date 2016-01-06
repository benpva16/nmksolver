# Piece.py
# Author: benpva16
# Date Created: 2015-12-24

class Piece:
    def __init__(self, kind, row, col):
        self.kind = kind
        self.row = row
        self.col = col
        self.seen = False

    def display_piece(self):
        piece_rank = 8 - self.row
        files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        piece_file = files[self.col]
        print('{} at row {}, col {}'.format(self.kind, piece_rank, piece_file))

    def get_capture_candidates(self, pieces):
        capture_candidates = []
        if self.kind.lower() == 'b':
            # Check all four diagonals until you hit a piece or the board edge
            # Northwest
            current_row = self.row
            current_col = self.col
            while True:
                current_row -= 1
                current_col -= 1
                if current_row < 0 or \
                   current_col < 0:
                    break
                candidate = next((x for x in pieces if (x.row == current_row and \
                    x.col == current_col)), None)
                if candidate is None or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            # Northeast
            current_row = self.row
            current_col = self.col
            while True:
                current_row -= 1
                current_col += 1
                if current_row < 0 or \
                   current_col > 7:
                    break
                candidate = next((x for x in pieces if (x.row == current_row and \
                    x.col == current_col)), None)
                if candidate is None or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            # Southwest
            current_row = self.row
            current_col = self.col
            while True:
                current_row += 1
                current_col -= 1
                if current_row > 7 or \
                   current_col < 0:
                    break
                candidate = next((x for x in pieces if (x.row == current_row and \
                    x.col == current_col)), None)
                if candidate is None or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            # Southeast
            current_row = self.row
            current_col = self.col
            while True:
                current_row += 1
                current_col += 1
                if current_row > 7 or \
                   current_col > 7:
                    break
                candidate = next((x for x in pieces if (x.row == current_row and \
                    x.col == current_col)), None)
                if candidate is None or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            return capture_candidates
        elif self.kind.lower() == 'n':
            knight_moves = []
            knight_moves.append((self.row-2, self.col-1))
            knight_moves.append((self.row-2, self.col+1))
            knight_moves.append((self.row-1, self.col-2))
            knight_moves.append((self.row-1, self.col+2))
            knight_moves.append((self.row+1, self.col-2))
            knight_moves.append((self.row+1, self.col+2))
            knight_moves.append((self.row+2, self.col-1))
            knight_moves.append((self.row+2, self.col+1))
            for p in pieces:
                piece_pos = (p.row, p.col)
                if piece_pos in knight_moves and not p.seen:
                    capture_candidates.append(p)
            return capture_candidates
        elif self.kind.lower() == 'r':
            # Check all four directions until you hit a piece or the board edge
            # North
            current_row = self.row
            while True:
                current_row -= 1
                if current_row < 0:
                    break
                candidate = next((x for x in pieces if (x.row == current_row and \
                    x.col == self.col)), None)
                if not candidate or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            # South
            current_row = self.row
            while True:
                current_row += 1
                if current_row > 7:
                    break
                candidate = next((x for x in pieces if (x.row == current_row and \
                    x.col == self.col)), None)
                if not candidate or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            # East
            current_col = self.col
            while True:
                current_col -= 1
                if current_col < 0:
                    break
                candidate = next((x for x in pieces if (x.row == self.row and \
                    x.col == current_col)), None)
                if not candidate or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            # West
            current_col = self.col
            while True:
                current_col += 1
                if current_col > 7:
                    break
                candidate = next((x for x in pieces if (x.row == self.row and \
                    x.col == current_col)), None)
                if not candidate or candidate.seen:
                    continue
                else:
                    capture_candidates.append(candidate)
            return capture_candidates
        else:
            return []