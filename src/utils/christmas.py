from utils.ColorUtil import *
from utils.matrix import Matrix
from utils.text import *
import utils.numbers as numbers
from utils.decorations import Decoration, MatrixDecoration


class ChristmasCounterDowner:

    def __init__(self, matrix: Matrix) -> None:
        super().__init__()
        self.matrix = matrix
        self.tc = GREEN
        self.nc = RED
        self._setup_text()

    def _setup_text(self):
        #  days
        d(24, 2, self.tc, self.matrix)
        a(29, 2, self.tc, self.matrix)
        y(33, 2, self.tc, self.matrix)
        s(37, 2, self.tc, self.matrix)
        #  till
        t(26, 8, self.tc, self.matrix)
        i(30, 8, self.tc, self.matrix)
        l(32, 8, self.tc, self.matrix)
        l(36, 8, self.tc, self.matrix)
        #  Christmas
        c(3, 15, self.tc, self.matrix)
        h(7, 15, self.tc, self.matrix)
        r(11, 15, self.tc, self.matrix)
        i(15, 15, self.tc, self.matrix)
        s(17, 15, self.tc, self.matrix)
        t(21, 15, self.tc, self.matrix)
        m(25, 15, self.tc, self.matrix)
        a(31, 15, self.tc, self.matrix)
        s(35, 15, self.tc, self.matrix)
        bang(39, 15, self.tc, self.matrix)
        self.matrix.show()

    def set_days(self, days_to_go: int):
        # get 100s place
        start = 6
        digits = []
        if days_to_go > 99:
            digits.append(int(days_to_go / 100))
            start = 0
        # get 10s place
        digit_2 = int(days_to_go/10)
        if digit_2 > 9:
            digit_2 = digit_2 % 10
        digits.append(digit_2)
        # get 1s place
        digits.append(days_to_go % 10)
        # draw each digit
        digit_width = 8
        for idx, digit in enumerate(digits):
            self._get_method(digit)(digit_width * idx + start, 0, self.nc, self.matrix)
        self.matrix.show()

    def _get_method(self, n: int):
        return getattr(numbers, f'_{n}')


class CandyCane(Decoration):

    def __init__(self, pixels, start: int, end: int):
        super().__init__(pixels, start, end)
        self.rows = []
        # setup rows
        if self.size == 100:
            # rows are laid out with every two being for the first half
            # along with every other in the second half with a one pixel row all the
            # way at the tip of the candy cane hook (last one)
            for x in range(0, 65, 2):
                self.rows.append([x, x+1])
            # the tip of the cane that is one pixel
            self.rows.append([66])
            # now back down, adding to the existing rows
            for x in range(0, 34):
                self.rows[33-x].append(66+x)
            self.row_num = len(self.rows)
        elif self.size == 200:
            # four columns of 50 (up, down, up down)
            # self.rows.append([1, 98, 101, 198])
            # self.rows.append([2, 97, 102, 197])
            # self.rows.append([49, 50, 149, 150])
            for x in range(50):
                self.rows.append([0+x, 99-x, 100+x, 199-x])
            self.row_num = len(self.rows)

    def stripes(self, color_list, width: int):
        i = 0
        j = 0
        for row in self.rows:
            c = color_list[i%len(color_list)]
            for n in row:
                self.pixels[n] = c
            if j < width - 1:
                j += 1
            else:
                i += 1
                j = 0
        self.pixels.show()


class Stocking(Decoration):

    def __init__(self, pixels, start: int, end: int, base_color, fringe_color):
        super().__init__(pixels, start, end)
        self.pixels[start: start + 28] = [base_color]*28
        self.pixels[start + 28: end] = [fringe_color]*22
        self.pixels.show()

def Santa(MatrixDecoration):
    
    def __init__(self, matrix: Matrix):
        super().__init__(matrix)
        self.draw(0,0)

    def draw(self, dx: int, dy: int):
        self.matrix.setPixels([10, 11, 12], [1], RED)
        self.matrix.setPixels([9, 10, 11, 12, 13], [2], RED)
        self.matrix.setPixels([8, 9, 10, 11, 12, 13, 14], [3], RED)
        self.matrix.setPixels([8, 9, 10, 11, 12, 13, 14], [4], WHITE)
        self.matrix.setPixels([8, 14], [5], WHITE)
        self.matrix.setPixels([9, 11, 13], [5], PINK)
        self.matrix.setPixels([10, 12], [5], BLUE)
        self.matrix.setPixels([8, 14], [6], WHITE)
        self.matrix.setPixels([10, 12], [6], PINK)
        self.matrix.setPixels([9, 11, 13], [6], LRED)
        self.matrix.setPixels([8, 10, 11, 12, 13, 14], [7], WHITE)
        self.matrix.setPixels([9, 13], [7], PINK)
        self.matrix.setPixels([8, 9, 10, 12, 13, 14], [8], PINK)
        self.matrix.setPixels([11], [8], LRED)
        self.matrix.setPixels([9, 10, 11, 12, 13], [9], WHITE)
        self.matrix.setPixels([9, 10, 11, 12, 13], [10], WHITE)
        self.matrix.setPixels([7, 8, 14, 15], [10], RED)
        self.matrix.setPixels([10, 11, 12], 11, WHITE)
        self.matrix.setPixels([7, 8, 9, 13, 14, 15], [11], RED)
        self.matrix.setPixels([7, 8, 9, 10, 11, 12, 13, 14, 15], [12], RED)
        self.matrix.setPixels([7, 8, 9, 10, 11, 12, 13, 14, 15], [13], RED)
        self.matrix.setPixels([11], [14], YELLOW)
        self.matrix.setPixels([8, 9, 10], [14], DBROWN)
        self.matrix.setPixels([12, 13, 14], [14], DBROWN)
        self.matrix.setPixels([7, 15], [14], LGRAY)
        self.matrix.setPixels([7, 15], [15], LGRAY)
        self.matrix.setPixels([8, 9, 10, 11, 12, 13, 14], [15], RED)
        self.matrix.setPixels([8, 9, 10, 11, 12, 13, 14], [16], RED)
        self.matrix.setPixels([8, 9, 10, 12, 13, 14], [17], RED)
        self.matrix.setPixels([8, 9, 10, 12, 13, 14], [18], RED)
        self.matrix.show()

    def _draw_body(self):
        pass

    def _draw_head(self):
        pass

    def _draw_arms(self):
        pass
