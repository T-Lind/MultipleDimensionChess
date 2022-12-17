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


    def print(self, i):
        for row in self.array[i]:
            for item in row:
                print(item.string, end=" ")
            print()
