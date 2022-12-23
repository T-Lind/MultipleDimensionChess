from vpython import *

from chess3d.Pieces import Piece

full_color = {"w": color.white, "b":color.black}

active_material = []
def reorient_offset(x, y, z):
    x *= 2
    y *= 2.05
    z *= 2

    # Base offset
    z += 1
    y += -7
    x += -6.9

    x, z = (z, x)
    y *= -1



    return x, y, z

def draw_knight(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    active_material.append(sphere(pos=vector(x, y, z), size=vector(1.1, 1.5, 1), color=full_color[color_str]))
    active_material.append(sphere(pos=vector(x+.1, y+.7, z+0), size=vector(1.1, 1.1, 1), color=full_color[color_str]))
    active_material.append(cylinder(pos=vector(x+.4, y+.7, z+0), size=vector(0.5, 0.4, 0.4), color=full_color[color_str]))
    active_material.append(cylinder(pos=vector(x, y-0.7, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str]))

def draw_bishop(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)
    # sphere(pos=vector(x, y, z), size=vector(1, 1.5, 1), color=full_color[color_str])
    active_material.append(cylinder(pos=vector(x, y-0.7, z), size=vector(0.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str]))
    active_material.append(sphere(pos=vector(x, y+0.1, z), size=vector(1.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str]))

def draw_pawn(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)
    active_material.append(cylinder(pos=vector(x, y, z), size=vector(1, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str]))

def draw_rook(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    active_material.append(cylinder(pos=vector(x, y, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str]))
    active_material.append(cylinder(pos=vector(x, y-0.5, z), size=vector(1, 0.75, 0.75), axis=vector(0, 1, 0), color=full_color[color_str]))

def draw_queen(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    active_material.append(cylinder(pos=vector(x, y - 0.7, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str]))
    active_material.append(sphere(pos=vector(x, y + 0.1, z), size=vector(1.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str]))
    active_material.append(cylinder(pos=vector(x, y+0.3, z), size=vector(0.1, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str]))
    active_material.append(cylinder(pos=vector(x, y+0.5, z), size=vector(0.1, 1.5, 1.5), axis=vector(0, 1, 0), color=color.yellow))

def draw_king(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    active_material.append(cylinder(pos=vector(x, y - 0.7, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str]))
    active_material.append(box(pos=vector(x, y+0.1, z), size=vector(0.3, 1.5, 0.3), color=color.yellow))
    active_material.append(box(pos=vector(x, y+0.5, z), size=vector(0.3, 0.3, 0.75), color=color.yellow))


draw_function = {
    "P": draw_pawn,
    "N": draw_knight,
    "B": draw_bishop,
    "R": draw_rook,
    "Q": draw_queen,
    "K": draw_king
}

def reset_graphics(board):
    for piece in active_material:
        piece.visible = False
    active_material.clear()
    for x in range(8):
        for y in range(8):
            for z in range(8):
                active_material.append(board.get(x, y, z))
                draw_piece(x, y, z, board.get(x, y, z))

def draw_piece(x, y, z, piece):
    try:
        return draw_function[piece.string[1]](x, y, z, piece.string[0])
    except Exception as _:
        pass

def draw_board(board) -> None:
    scene = canvas()
    scene.caption = "3D Chess using VPython"
    scene.userpan = True
    scene.userspin = True

    side = 8
    thk = 0.1
    s2 = 2 * side - thk
    s3 = 2 * side + thk

    verticals = []
    horizontals = []
    delimiters = []

    for i in range(2, 15, 2):
        verticals.append(box(pos=vector(i, 0, 0), size=vector(thk, s2, s3), color=color.blue, opacity=0.3, emissivity=True))
        local_light(pos=vector(i, 0, 0), color=color.white)

    for i in range(-6, 7, 2):
        horizontals.append(box(pos=vector(8, i, 0), size=vector(s2, thk, s3), color=color.red, opacity=0.3, emissivity=True))

        for j in range(-8, 9, 2):
            delimiters.append(box(pos=vector(8, i, j), size=vector(16, thk, thk), color=color.black, opacity=0.5, emissivity=True))

    box(pos=vector(0, 8, -8), size=vector(thk, thk, thk), color=color.green, opacity=1, emissivity=True)

    for x in range(8):
        for y in range(8):
            for z in range(8):
                active_material.append(board.get(x, y, z))
                draw_piece(x, y, z, board.get(x, y, z))

