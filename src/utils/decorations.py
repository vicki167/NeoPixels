from matrix import Matrix

class Decoration:

    def __init__(self, pixels, start: int, end: int):
        self.pixels = pixels
        self.start = start
        self.end = end
        self.size = end - start + 1


class MatrixDecoration:

    def __init__(self, matrix: Matrix):
        self.matrix = matrix
