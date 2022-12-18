import numpy as np

from chess3d.Pieces import Piece

WHITE = Piece.WHITE
BLACK = Piece.BLACK


# First index is x axis (away from pieces), second is y (vertical), second is z (along pieces)
class Board:
    def __init__(self):
        self.array = np.full((8, 8, 8), Piece.NONE, dtype=Piece)

        # Fill with pawns
        for i in range(8):
            self.array[i][1][0] = WHITE.PAWN
            self.array[i][0][1] = WHITE.PAWN

            self.array[i][7][6] = BLACK.PAWN
            self.array[i][6][7] = BLACK.PAWN

        self.array[0][0][0] = WHITE.ROOK
        self.array[7][0][0] = WHITE.ROOK

        self.array[1][0][0] = WHITE.KNIGHT
        self.array[2][0][0] = WHITE.BISHOP
        self.array[3][0][0] = WHITE.QUEEN
        self.array[4][0][0] = WHITE.KING
        self.array[5][0][0] = WHITE.BISHOP
        self.array[6][0][0] = WHITE.KNIGHT

        self.array[0][7][7] = BLACK.ROOK
        self.array[7][7][7] = BLACK.ROOK

        self.array[1][7][7] = BLACK.KNIGHT
        self.array[2][7][7] = BLACK.BISHOP
        self.array[3][7][7] = BLACK.QUEEN
        self.array[4][7][7] = BLACK.KING
        self.array[5][7][7] = BLACK.BISHOP
        self.array[6][7][7] = BLACK.KNIGHT

    def print(self, i):
        for row in self.array[i]:
            for item in row:
                print(item.string, end=" ")
            print()
