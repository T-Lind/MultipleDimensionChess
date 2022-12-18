import numpy as np

from chess3d.Pieces import Piece
from chess3d.Exceptions import MovementException
WHITE = Piece.WHITE
BLACK = Piece.BLACK


# First index is x axis (away from pieces), second is y (vertical), second is z (along pieces)
class Board:
    def __init__(self):
        self.array = np.full((8, 8, 8), Piece.NONE, dtype=Piece)

        self.captured_material = {"w":0, "b":0}

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

    def print_slice(self, i) -> None:
        for row in self.array[i]:
            for item in row:
                print(item.string, end=" ")
            print()

    def set(self, x, y, z, piece):
        self.array[x][y][z] = piece
    def get(self, x, y, z):
        return self.array[x][y][z]

    def print_cube(self) -> None:
        for slice in range(8):
            self.print_slice(slice)
            print(end="\n\n")

    def check_filled(self, player, x, y, z) -> bool:
        return self.array[x][y][z].type == player.type

    def move(self, player, pos, to) -> None:
        # Only move if the starting location selected is of the type specified
        if self.check_filled(player, *pos):
            # Only move to the other position if it is not filled with a piece of the same type
            if not self.check_filled(player, *to):
                if self.check_filled(Piece.opposite(player), *to):
                    # Keep track of material score when capturing
                    self.captured_material[player.type] += self.get(*to).material
                # Move the piece from `pos` to `to`
                self.set(*to, self.get(*pos))
            else:
                raise MovementException("Location selected to move is filled with the same piece color")
        else:
            raise MovementException("Piece selected to move was not of correct type")
