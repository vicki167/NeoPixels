from .ColorUtil import *


def draw_heart(dx, dy, matrix, size=10, color=RED):
    if size == 10:
        draw_heart_10(dx, dy, matrix, color)
    elif size == 20:
        draw_heart_20(dx, dy, matrix, color)

def draw_heart_10(dx, dy, matrix, color=RED):
    print(f'draw_heart_10')
    # row 0
    matrix.setPixel(2+dx, 0+dy, color)
    matrix.setPixel(3+dx, 0+dy, color)
    matrix.setPixel(5+dx, 0+dy, color)
    matrix.setPixel(6+dx, 0+dy, color)
    # row 1
    for x in range(1, 8):
        matrix.setPixel(x+dx, 1+dy, color)
    # row 2-5
    for y in range(2, 6):
        for x in range(0, 9):
            matrix.setPixel(x+dx, y+dy, color)
    # row 6
    for x in range(1, 8):
        matrix.setPixel(x+dx, 6+dy, color)
    # row 7
    for x in range(2, 7):
        matrix.setPixel(x+dx, 7+dy, color)
    # row 8
    for x in range(3, 6):
        matrix.setPixel(x+dx, 8+dy, color)
    # row 9
    matrix.setPixel(4+dx, 9+dy, color)


def draw_heart_20(dx, dy, matrix, color=RED):
    print(f'draw_heart_20')
    # row 0-1
    for y in [0, 1]:
        for x in range(4, 9):
            matrix.setPixel(x+dx, y+dy, color)
        for x in range(11, 16):
            matrix.setPixel(x+dx, y+dy, color)
    # row 2-3
    for y in [2, 3]:
        for x in range(2, 18):
            matrix.setPixel(x+dx, y+dy, color)
    # row 4-11
    for y in range(4, 12):
        for x in range(0, 20):
            matrix.setPixel(x+dx, y+dy, color)
    # row 12-13
    for y in [12, 13]:
        for x in range(2, 18):
            matrix.setPixel(x+dx, y+dy, color)
    # row 14-15
    for y in [14, 15]:
        for x in range(4, 16):
            matrix.setPixel(x+dx, y+dy, color)
    # row 16-17
    for y in [16, 17]:
        for x in range(7, 13):
            matrix.setPixel(x+dx, y+dy, color)
    # row 18
    matrix.setPixel(9+dx, 18+dy, color)
    matrix.setPixel(10+dx, 18+dy, color)
