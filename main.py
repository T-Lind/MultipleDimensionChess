from vpython import *
from chess3d import draw_board

full_color = {"w": color.white, "b":color.black}


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

    sphere(pos=vector(x, y, z), size=vector(1.1, 1.5, 1), color=full_color[color_str])
    sphere(pos=vector(x+.1, y+.7, z+0), size=vector(1.1, 1.1, 1), color=full_color[color_str])
    cylinder(pos=vector(x+.4, y+.7, z+0), size=vector(0.5, 0.4, 0.4), color=full_color[color_str])
    cylinder(pos=vector(x, y-0.7, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str])

def draw_bishop(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)
    # sphere(pos=vector(x, y, z), size=vector(1, 1.5, 1), color=full_color[color_str])
    cylinder(pos=vector(x, y-0.7, z), size=vector(0.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str])
    sphere(pos=vector(x, y+0.1, z), size=vector(1.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str])

def draw_pawn(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)
    cylinder(pos=vector(x, y, z), size=vector(1, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str])

def draw_rook(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    cylinder(pos=vector(x, y, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str])
    cylinder(pos=vector(x, y-0.5, z), size=vector(1, 0.75, 0.75), axis=vector(0, 1, 0), color=full_color[color_str])

def draw_queen(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    cylinder(pos=vector(x, y - 0.7, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str])
    sphere(pos=vector(x, y + 0.1, z), size=vector(1.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str])
    cylinder(pos=vector(x, y+0.3, z), size=vector(0.1, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str])
    cylinder(pos=vector(x, y+0.5, z), size=vector(0.1, 1.5, 1.5), axis=vector(0, 1, 0), color=color.yellow)

def draw_king(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)

    cylinder(pos=vector(x, y - 0.7, z), size=vector(0.5, 1.5, 1.5), axis=vector(0, 1, 0), color=full_color[color_str])
    box(pos=vector(x, y+0.1, z), size=vector(0.3, 1.5, 0.3), color=color.yellow)
    box(pos=vector(x, y+0.5, z), size=vector(0.3, 0.3, 0.75), color=color.yellow)

if __name__ == '__main__':
    draw_board()

    draw_king(0, 0, 0, "w")

    # +X
    draw_rook(7, 0, 0, "w")

    # +Y
    draw_queen(0, 6, 0, "w")

    # +Z
    draw_bishop(0, 0, 7, "w")


    draw_pawn(7, 7, 7, "w")

    input()
