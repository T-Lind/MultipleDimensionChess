from chess3d.Board import Board
from chess3d.Pieces import Piece
board = Board()

if __name__ == '__main__':
    print(board.array[1][1][0].string)
    print(board.check_filled(Piece.WHITE, 5, 1, 1))
    # board.print_cube()
