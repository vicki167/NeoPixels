from .matrix import Matrix

#  default is 7 X 14
#  0123456


def one(dx, dy, color, matrix: Matrix):
    # put all the way to the right
    for y in range(14):
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def two(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(8):
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


def three(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(8):
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


def four(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in [2, 3, 4]:
        matrix.setPixel(x+dx, 6+dy, color)
        matrix.setPixel(x+dx, 7+dy, color)
    # vertical parts left to draw
    for y in range(14):
        if y < 6:
            matrix.setPixel(0+dx, y+dy, color)
            matrix.setPixel(1+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)
        matrix.setPixel(7+dx, y+dy, color)


def five(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(8):
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


def six(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(8):
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


def seven(dx, dy, color, matrix: Matrix):
    # horizontal parts
    for x in range(8):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 1+dy, color)
    for y in range(2, 14):
        matrix.setPixel(5+dx, y+dy, color)
        matrix.setPixel(6+dx, y+dy, color)


def eight(dx, dy, color, matrix: Matrix):
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


def nine(dx, dy, color, matrix: Matrix):
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


def zero(dx, dy, color, matrix: Matrix):
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

