from chess3d.Board import Board
from chess3d.Pieces import Piece
board = Board()

if __name__ == '__main__':
    # print(board.array[1][1][0].string)
    # board.set(5, 5, 5, Piece.WHITE.ROOK())
    # print(board.is_legal_movement((5, 5, 5), (5, 5, 6)))
    board.print_cube()
