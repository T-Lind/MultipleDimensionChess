class Piece:
    class NONE:
        string = " "
        value = 0
        pass

    class WHITE:
        class PAWN:
            string = "wP"

        class KNIGHT:
            string = "wN"

        class BISHOP:
            string = "wB"

        class ROOK:
            string = "wR"

        class QUEEN:
            string = "wQ"

        class KING:
            string = "wK"

    class BLACK:
        class PAWN:
            string = "bP"

        class KNIGHT:
            string = "bN"

        class BISHOP:
            string = "bB"

        class ROOK:
            string = "bR"

        class QUEEN:
            string = "bQ"

        class KING:
            string = "bK"