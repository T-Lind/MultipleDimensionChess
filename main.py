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
    sphere(pos=vector(x, y, z+0.1), size=vector(1.5, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str])

def draw_pawn(x, y, z, color_str):
    x, y, z = reorient_offset(x, y, z)
    # sphere(pos=vector(x, y, z), size=vector(1, 1.5, 1), color=full_color[color_str])
    cylinder(pos=vector(x, y, z), size=vector(1, 0.75, 1), axis=vector(0, 1, 0), color=full_color[color_str])



if __name__ == '__main__':
    draw_board()
    # Knight
    draw_knight(0, 0, 0, "w")

    # +X
    draw_knight(7, 0, 0, "w")

    # +Y
    draw_bishop(0, 6, 0, "w")

    # +Z
    draw_bishop(0, 0, 7, "w")


    draw_pawn(7, 7, 7, "w")

    input()
