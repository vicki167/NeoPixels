from .matrix import Matrix


def a(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(2+dx, y+dy, color)
    matrix.setPixel(1+dx, 0+dy, color)
    matrix.setPixel(1+dx, 2+dy, color)


def b(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(2+dx, y+dy, color)
    matrix.setPixel(1+dx, 0+dy, color)
    matrix.setPixel(1+dx, 2+dy, color)
    matrix.setPixel(1+dx, 4+dy, color)


def c(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
    matrix.setPixel(1+dx, 0+dy, color)
    matrix.setPixel(2+dx, 0+dy, color)
    matrix.setPixel(1+dx, 4+dy, color)
    matrix.setPixel(2+dx, 4+dy, color)


def d(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        if y in [1, 2, 3]:
            matrix.setPixel(3+dx, y+dy, color)
    matrix.setPixel(1+dx, 0+dy, color)
    matrix.setPixel(2+dx, 0+dy, color)
    matrix.setPixel(1+dx, 4+dy, color)
    matrix.setPixel(2+dx, 4+dy, color)


def h(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(2+dx, y+dy, color)
    matrix.setPixel(1+dx, 2+dy, color)


def i(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)


def l(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
    matrix.setPixel(1+dx, 4+dy, color)
    matrix.setPixel(2+dx, 4+dy, color)


def m(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(4+dx, y+dy, color)
    matrix.setPixel(1+dx, 1+dy, color)
    matrix.setPixel(3+dx, 1 +dy, color)
    matrix.setPixel(2+dx, 2 +dy, color)
    matrix.setPixel(2+dx, 3 +dy, color)


def o(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        matrix.setPixel(2+dx, y+dy, color)
    matrix.setPixel(1+dx, 0+dy, color)
    matrix.setPixel(1+dx, 4+dy, color)


def p(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        if y < 3:
            matrix.setPixel(2+dx, y+dy, color)


def r(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(0+dx, y+dy, color)
        if y not in [3]:
            matrix.setPixel(2+dx, y+dy, color)
    matrix.setPixel(1+dx, 3+dy, color)


def s(dx, dy, color, matrix: Matrix):
    for x in range(0, 3):
        matrix.setPixel(x+dx, 0+dy, color)
        matrix.setPixel(x+dx, 2+dy, color)
        matrix.setPixel(x+dx, 4+dy, color)
    matrix.setPixel(0+dx, 1+dy, color)
    matrix.setPixel(2+dx, 3+dy, color)


def t(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        matrix.setPixel(1+dx, y+dy, color)
    matrix.setPixel(0+dx, 0+dy, color)
    matrix.setPixel(2+dx, 0 +dy, color)


def y(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        if y < 3:
            matrix.setPixel(0+dx, y+dy, color)
            matrix.setPixel(2+dx, y+dy, color)
        if y > 2:
            matrix.setPixel(1 + dx, y + dy, color)


def bang(dx, dy, color, matrix: Matrix):
    for y in range(0,5):
        if y < 3:
            if y != 3:
                matrix.setPixel(0+dx, y+dy, color)
            matrix.setPixel(2+dx, y+dy, color)

