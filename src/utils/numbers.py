from utils.matrix import Matrix

#  default is 7 X 14
#  0123456


def _1(dx, dy, color, matrix: Matrix):
    # put all the way to the right
    for y in range(14):
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _2(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(7):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
        matrix.setPixel(x+dx, 12+dy, color)
        matrix.setPixel(x+dx, 13+dy, color)
    # vertical parts left to draw
    for y in [2, 3, 4, 5]:
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)
    for y in [8, 9, 10, 11]:
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(1+dx, y+dy, color)


def _3(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(7):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        if x not in [0, 1]:
            matrix.setPixel(x+dx, 6+dy, color)
            matrix.setPixel(x+dx, 7+dy, color)
        matrix.setPixel(x+dx, 12+dy, color)
        matrix.setPixel(x+dx, 13+dy, color)
    # vertical parts left to draw
    for y in [2, 3, 4, 5, 8, 9, 10, 11]:
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _4(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in [2, 3, 4]:
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
    # vertical parts left to draw
    for y in range(14):
        if y < 8:
            matrix.setPixel(0+dx, y+dy, color)
            matrix.setPixel(1+dx, y+dy, color)
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _5(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(7):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
        matrix.setPixel(x+dx, 12+dy, color)
        matrix.setPixel(x+dx, 13+dy, color)
    # vertical parts left to draw
    for y in [2, 3, 4, 5]:
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(1+dx, y+dy, color)
    for y in [8, 9, 10, 11]:
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _6(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(7):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
        matrix.setPixel(x+dx, 12+dy, color)
        matrix.setPixel(x+dx, 13+dy, color)
    # vertical parts left to draw
    for y in [2, 3, 4, 5]:
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(1+dx, y+dy, color)
    for y in [8, 9, 10, 11]:
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(1+dx, y+dy, color)
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _7(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(7):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
    for y in range(2, 14):
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _8(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in [2, 3, 4]:
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
        matrix.setPixel(x+dx, 12+dy, color)
        matrix.setPixel(x+dx, 13+dy, color)
    for y in range(0, 14):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(1+dx, y+dy, color)
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _9(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in [2, 3, 4]:
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
    for y in range(0, 14):
        if y < 8:
            matrix.setPixel(0+dx, y+dy, color)
            matrix.setPixel(1+dx, y+dy, color)
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _0(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in [2, 3, 4]:
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
        matrix.setPixel(x+dx, 12+dy, color)
        matrix.setPixel(x+dx, 13+dy, color)
    for y in range(0, 14):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(1+dx, y+dy, color)
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def _99(dx, dy):
    print(f'dx: {dx}, dy: {dy}')
