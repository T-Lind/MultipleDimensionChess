from chess3d.Exceptions import LogicException

class Piece:
    class NONE:
        type = ""
        string = " "
        pass

    class WHITE:
        type = "w"

        class PAWN:
            type = "w"
            string = "wP"
            material = 1

        class KNIGHT:
            type = "w"
            string = "wN"
            material = 4

        class BISHOP:
            type = "w"
            string = "wB"
            material = 4

        class ROOK:
            type = "w"
            string = "wR"
            material = 5

        class QUEEN:
            type = "w"
            string = "wQ"
            material = 9

        class KING:
            type = "w"
            string = "wK"
            material = 0

    class BLACK:
        type = "b"

        class PAWN:
            type = "b"
            string = "bP"
            material = 1

        class KNIGHT:
            type = "b"
            string = "bN"
            material = 4

        class BISHOP:
            type = "b"
            string = "bB"
            material = 4

        class ROOK:
            type = "b"
            string = "bR"
            material = 5

        class QUEEN:
            type = "b"
            string = "bQ"
            material = 9

        class KING:
            type = "b"
            string = "bK"
            material = 0

    @staticmethod
    def opposite(type):
        if type == Piece.BLACK:
            return Piece.WHITE
        if type == Piece.WHITE:
            return Piece.BLACK
        raise LogicException("Improper piece type specified")