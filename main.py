from vpython import *
from chess3d import draw_board, draw_piece
from chess3d.Board import Board
from chess3d.Graphics import reset_graphics
from chess3d.InputMove import black_move, white_move

if __name__ == '__main__':
    board = Board()
    draw_board()

    for _ in range(10):
        reset_graphics(board)
        white_move(board)
        reset_graphics(board)
        black_move(board)

    input()
