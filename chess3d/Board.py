import numpy as np
from math import hypot

from chess3d.Pieces import Piece
from chess3d.Exceptions import MovementException

WHITE = Piece.WHITE
BLACK = Piece.BLACK


# First index is x axis (away from pieces), second is y (vertical), second is z (along pieces)
class Board:
    def __init__(self):
        self.array = np.full((8, 8, 8), Piece.NONE(), dtype=Piece)

        self.move = 0

        self.captured_material = {"w": 0, "b": 0}

        # Fill with pawns
        for i in range(8):
            self.array[i][1][0] = WHITE.PAWN()
            self.array[i][0][1] = WHITE.PAWN()

            self.array[i][7][6] = BLACK.PAWN()
            self.array[i][6][7] = BLACK.PAWN()

        self.array[0][0][0] = WHITE.ROOK()
        self.array[7][0][0] = WHITE.ROOK()

        self.array[1][0][0] = WHITE.KNIGHT()
        self.array[2][0][0] = WHITE.BISHOP()
        self.array[3][0][0] = WHITE.QUEEN()
        self.array[4][0][0] = WHITE.KING()
        self.array[5][0][0] = WHITE.BISHOP()
        self.array[6][0][0] = WHITE.KNIGHT()

        self.array[0][7][7] = BLACK.ROOK()
        self.array[7][7][7] = BLACK.ROOK()

        self.array[1][7][7] = BLACK.KNIGHT()
        self.array[2][7][7] = BLACK.BISHOP()
        self.array[3][7][7] = BLACK.QUEEN()
        self.array[4][7][7] = BLACK.KING()
        self.array[5][7][7] = BLACK.BISHOP()
        self.array[6][7][7] = BLACK.KNIGHT()

    def print_slice(self, i) -> None:
        for row in self.array[i]:
            for item in row:
                print(item.string, end=" ")
            print()

    def set(self, x, y, z, piece) -> None:
        self.array[x][y][z] = piece

    def get(self, x, y, z) -> Piece:
        return self.array[x][y][z]

    def print_cube(self) -> None:
        for slice in range(8):
            self.print_slice(slice)
            print(end="\n\n")

    def check_filled(self, player, x, y, z) -> bool:
        return self.array[x][y][z].string[0] == player.type

    def move(self, player, pos, to) -> None:
        # Only move if the starting location selected is of the type specified
        if self.check_filled(player, *pos):
            # Only move to the other position if it is not filled with a piece of the same type
            if not self.check_filled(player, *to):
                if self.check_filled(Piece.opposite(player), *to):
                    # Keep track of material score when capturing
                    self.captured_material[player.string[0]] += self.get(*to).material
                if self.is_legal_movement(pos, to, self.get(*pos)):
                    # Move the piece from `pos` to `to`
                    self.set(*to, self.get(*pos))
            else:
                raise MovementException("Location selected to move is filled with the same piece color")
        else:
            raise MovementException("Piece selected to move was not of correct type")

    def is_legal_movement(self, pos, to) -> bool:
        piece = self.get(*pos)
        # TODO: Finish this legal movement code, need to do for pawns, bishops, knights, and queens
        pos_set = set(pos)
        to_set = set(to)
        # Coordinates should not be the same.
        if pos == to:
            return False
        # Coordinates should not be out of bounds
        if min(pos_set.union(to_set)) < 0 or max(pos_set.union(to_set)) > 7:
            return False

        if piece.string[1] == "P":
            if piece.string[0] == "w":
                # White case
                if pos[2] != to[2]:
                    # If the piece is not black then it is an illegal move
                    if self.get(*to).string[0] != "b":
                        return False
                    # TODO: Check and see if the take is valid
                else:
                    if self.move == 0:
                        # TODO: Implement moving two spaces in first move
                        pass
                    # Not a take - moving one away in either direction
                    if to[0] - pos[0] == 1 ^ to[1] - pos[1] == 1:
                        return True


            elif piece.string[0] == "b":
                # Black case
                if pos[2] != to[2]:
                    # If the piece is not white then it is an illegal move
                    if self.get(*to).string[0] != "w":
                        return False
                    # TODO: Check and see if the take is valid
                else:
                    if self.move == 0:
                        # TODO: Implement moving two spaces in first move
                        pass
                    # Not a take - moving one away in either direction
                    if to[0] - pos[0] == -1 ^ to[1] - pos[1] == -1:
                        return True

        elif piece.string[1] == "B":
            differences = [pos[i] - to[i] for i in range(3)]
            # TODO: Finish bishop analyzing

        # Rook case
        elif piece.string[1] == "R":
            # Final position should have two coordinates in common
            return sum(x == y for x, y in zip(pos, to)) > 1

        # King case
        elif piece.string[1] == "K":
            # Final position should be one difference in any direction, including diagonals
            hypot1 = hypot(to[0] - pos[0], to[1] - pos[1])
            hypot2 = hypot(to[0] - pos[0], to[2] - pos[2])
            distance = hypot(hypot1, hypot2) - 1E-7  # Subtracting term is for floating point errors
            print("Distance", distance)
            return distance < 2
