from utils.matrix import Matrix

class Decoration:

    def __init__(self, pixels, start: int, end: int):
        self.pixels = pixels
        self.start = start
        self.end = end
        self.size = end - start + 1

    def show(self):
        self.pixels.show()

    def fill(self, color):
        self.pixels.fill(color)
        self.show()


class MatrixDecoration:

    def __init__(self, matrix: Matrix):
        self.matrix = matrix
