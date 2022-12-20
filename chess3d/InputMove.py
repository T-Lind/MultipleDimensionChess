from chess3d.Board import Board, WHITE, BLACK


def protected(_in, _type):
    try:
        return _type(_in)
    except Exception as e:
        print(e)
        return -1

def make_move(board, player) -> bool:
    x0 = protected(input("Enter the x coordinate to move from: "), int)
    y0 = protected(input("Enter the y coordinate to move from: "), int)
    z0 = protected(input("Enter the z coordinate to move from: "), int)

    print("Select the location to move to:")
    x1 = protected(input("Enter the x coordinate to move to: "), int)
    y1 = protected(input("Enter the y coordinate to move to: "), int)
    z1 = protected(input("Enter the z coordinate to move to: "), int)

    if min([x0, y0, z0, x1, y1, z1]) == -1:
        return False

    # board.unprotected_move(player, (x0, y0, z0), (x1, y1, z1))
    board.move_piece(player, (x0, y0, z0), (x1, y1, z1))

    return True

def white_move(board: Board):
    print("WHITE MOVE:\nSelect the piece to move:")

    completed = make_move(board, WHITE)
    while not completed:
        print("ERROR: INVALID MOVE SPECIFIED. TRY AGAIN.")
        completed = make_move(board, WHITE)


def black_move(board: Board):
    print("BLACK MOVE:\nSelect the piece to move:")
    completed = make_move(board, BLACK)
    while not completed:
        print("ERROR: INVALID MOVE SPECIFIED. TRY AGAIN.")
        completed = make_move(board, BLACK)

