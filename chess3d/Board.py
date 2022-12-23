from math import hypot

import numpy as np

from chess3d.Exceptions import MovementException
from chess3d.Pieces import Piece

WHITE = Piece.WHITE
BLACK = Piece.BLACK


# First index is x axis (along pieces), second is y (vertical), third is z (away from pieces)
class Board:
    def __init__(self):
        self.array = np.full((8, 8, 8), Piece.NONE(), dtype=Piece)

        self.move = 0

        self.captured_material = {"w": 0, "b": 0}

        # Fill with pawns
        for i in range(8):
            self.array[i][1][0] = WHITE.PAWN()
            self.array[i][0][1] = WHITE.PAWN()
            self.array[i][1][1] = WHITE.PAWN()

            self.array[i][7][6] = BLACK.PAWN()
            self.array[i][6][7] = BLACK.PAWN()
            self.array[i][6][6] = BLACK.PAWN()

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

    def unprotected_move(self, player, pos, to) -> None:
        # Only move if the starting location selected is of the type specified
        if self.check_filled(player, *pos):
            if self.check_filled(Piece.opposite(player), *to):
                # Keep track of material score when capturing
                self.captured_material[player.type] += self.get(*to).material
            self.set(*to, self.get(*pos))
            self.set(*pos, Piece.NONE)
        else:
            raise MovementException("Piece selected to move was not of correct type")

    def move_piece(self, player, pos, to) -> None:
        # Only move if the starting location selected is of the type specified
        if self.check_filled(player, *pos):
            if self.is_legal_movement(pos, to):
                if self.check_filled(Piece.opposite(player), *to):
                    # Keep track of material score when capturing
                    self.captured_material[player.type] += self.get(*to).material
                self.set(*to, self.get(*pos))
                self.set(*pos, Piece.NONE)
            else:
                print("Illegal Movement!")
        else:
            raise MovementException("Piece selected to move was not of correct type")

    def is_legal_movement(self, pos, to) -> bool:
        piece = self.get(*pos)
        print(piece)

        # TODO: Finish this legal movement code, need to do for pawns only now

        # Coordinates should not be out of bounds
        if min(pos + to) < 0 or max(pos + to) > 7:
            return False

        # Pawn case
        if piece.string[1] == "P":
            differences = [pos[i] - to[i] for i in range(3)]

            if piece.string[0] == "w":
                if self.move == 1:
                    if 0 <= differences[1] <= 2 and 0 <= differences[2] <= 2 and differences[0] == 0:
                        # Move down and away from starting
                        return True
                    return False
                else:
                    # After the first move benefit, must move one in either/or direction
                    if 0 <= differences[1] <= 1 and 0 <= differences[2] <= 1:
                        # If trying to move in x dimension - can only do while taking
                        if abs(differences[0]) == 1:
                            if self.get(*to).string[0] == "b":
                                # Capturing a black piece - this is valid
                                return True
                            else:
                                # Not capturing so invalid movement
                                return False
                        # Just a normal move so yes, it's fine
                        return True
                    # Invalid move to begin with
                    return False

            if piece.string[0] == "b":
                if self.move == 1:
                    if -2 <= differences[1] <= 0 and -2 <= differences[2] <= 0 and differences[0] == 0:
                        # Move down and away from starting
                        return True
                    return False
                else:
                    # After the first move benefit, must move one in either/or direction
                    if -1 <= differences[1] <= 0 and -1 <= differences[2] <= 0:
                        # If trying to move in x dimension - can only do while taking
                        if abs(differences[0]) == 1:
                            if self.get(*to).string[0] == "w":
                                # Capturing a black piece - this is valid
                                return True
                            else:
                                # Not capturing so invalid movement
                                return False
                        # Just a normal move so yes, it's fine
                        return True
                    # Invalid move to begin with
                    return False

        # Bishop case
        elif piece.string[1] == "B":
            differences = [abs(pos[i] - to[i]) for i in range(3)]
            return differences.count(differences[0]) == 3

        # Knight case
        elif piece.string[1] == "N":
            differences = [abs(pos[i] - to[i]) for i in range(3)]
            return differences.count(0) == 1 and differences.count(1) == 1 and differences.count(2) == 1

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
            return distance < 2

        elif piece.string[1] == "Q":
            differences = [abs(pos[i] - to[i]) for i in range(3)]
            if differences.count(differences[0]) == 3:
                return True
            return sum(x == y for x, y in zip(pos, to)) > 1

        raise MovementException("Uncaught piece movement check exception!")
