from chess3d.Exceptions import LogicException


class Piece:
    class NONE:
        type = ""
        string = " "
        pass

    class WHITE:
        type = "w"

        class PAWN:
            def __init__(self):
                self.string = "wP"
                self.material = 1
                self.move = 0

        class KNIGHT:
            def __init__(self):
                self.string = "wN"
                self.material = 4

        class BISHOP:
            def __init__(self):
                self.string = "wB"
                self.material = 4

        class ROOK:
            def __init__(self):
                self.string = "wR"
                self.material = 5

        class QUEEN:
            def __init__(self):
                self.string = "wQ"
                self.material = 9

        class KING:
            def __init__(self):
                self.string = "wK"
                self.material = 0

    class BLACK:
        type = "b"

        class PAWN:
            def __init__(self):
                self.string = "bP"
                self.material = 1
                self.move = 0

        class KNIGHT:
            def __init__(self):
                self.string = "bN"
                self.material = 4

        class BISHOP:
            def __init__(self):
                self.string = "bB"
                self.material = 4

        class ROOK:
            def __init__(self):
                self.string = "bR"
                self.material = 5

        class QUEEN:
            def __init__(self):
                self.string = "bQ"
                self.material = 9

        class KING:
            def __init__(self):
                self.string = "bK"
                self.material = 0

    @staticmethod
    def opposite(type):
        if type == Piece.BLACK:
            return Piece.WHITE
        if type == Piece.WHITE:
            return Piece.BLACK
        raise LogicException("Improper piece type specified")
