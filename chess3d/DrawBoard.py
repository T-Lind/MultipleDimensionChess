from vpython import *


def draw_board():
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
        verticals.append(box(pos=vector(i, 0, 0), size=vector(thk, s2, s3), color=color.blue, opacity=0.3))
        local_light(pos=vector(i, 0, 0), color=color.white)

    for i in range(-6, 7, 2):
        horizontals.append(box(pos=vector(8, i, 0), size=vector(s2, thk, s3), color=color.red, opacity=0.3))

        for j in range(-8, 9, 2):
            delimiters.append(box(pos=vector(8, i, j), size=vector(16, thk, thk), color=color.black, opacity=0.5))

    box(pos=vector(0, -8, -8), size=vector(thk, thk, thk), color=color.green, opacity=1)
