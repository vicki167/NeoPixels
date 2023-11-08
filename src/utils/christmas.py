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


class Santa(MatrixDecoration):
    
    def __init__(self, matrix: Matrix, x_pos: int = 0, y_pos: int = 0):
        super().__init__(matrix)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.draw(self.x_pos, self.y_pos)

    def draw(self, dx: int, dy: int):
        self.matrix.fill(OFF)
        dx -= 7
        self.matrix.setPixels([n+dx+self.x_pos for n in [10, 11, 12]], [0+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [9, 10, 11, 12, 13]], [1+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 11, 12, 13, 14]], [2+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 11, 12, 13, 14]], [3+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 14]], [4+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [9, 11, 13]], [4+dy], PINK)
        self.matrix.setPixels([n+dx+self.x_pos for n in [10, 12]], [4+dy], BLUE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 14]], [5+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [10, 12]], [5+dy], PINK)
        self.matrix.setPixels([n+dx+self.x_pos for n in [9, 11, 13]], [5+dy], LRED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 10, 11, 12, 13, 14]], [6+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [9, 13]], [6+dy], PINK)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 12, 13, 14]], [7+dy], PINK)
        self.matrix.setPixels([n+dx+self.x_pos for n in [11]], [7+dy], LRED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [9, 10, 11, 12, 13]], [8+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [9, 10, 11, 12, 13]], [9+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 14]], [9+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [10, 11, 12]], [10+dy], WHITE)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 13, 14]], [10+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 11, 12, 13, 14]], [11+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 11, 12, 13, 14]], [12+dy], RED)
        # belt
        self.matrix.setPixels([n+dx+self.x_pos for n in [11]], [13+dy], YELLOW)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10]], [13+dy], DBROWN)
        self.matrix.setPixels([n+dx+self.x_pos for n in [12, 13, 14]], [13+dy], DBROWN)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 11, 12, 13, 14]], [14+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 11, 12, 13, 14]], [15+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 12, 13, 14]], [16+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 12, 13, 14]], [17+dy], RED)
        self.matrix.setPixels([n+dx+self.x_pos for n in [8, 9, 10, 12, 13, 14]], [18+dy], DBROWN)
        self.matrix.setPixels([n+dx+self.x_pos for n in [7, 8, 9, 10, 12, 13, 14, 15]], [19+dy], DBROWN)
        # draw arms
        self._draw_left_arm(dx, dy)
        self._draw_right_arm(dx, dy)
        self.matrix.show()

    def _draw_body(self):
        pass

    def _draw_head(self):
        pass

    def _draw_left_arm(self, dx, dy):
        self.matrix.setPixel(7+dx, 9+dy, RED)
        self.matrix.setPixel(7+dx, 10+dy, RED)
        self.matrix.setPixel(7+dx, 11+dy, RED)
        self.matrix.setPixel(7+dx, 12+dy, RED)
        self.matrix.setPixel(7+dx, 13+dy, LGRAY)
        self.matrix.setPixel(7+dx, 14+dy, LGRAY)

    def _draw_right_arm(self, dx, dy):
        self.matrix.setPixel(15+dx, 9+dy, RED)
        self.matrix.setPixel(15+dx, 10+dy, RED)
        self.matrix.setPixel(15+dx, 11+dy, RED)
        self.matrix.setPixel(15+dx, 12+dy, RED)
        self.matrix.setPixel(15+dx, 13+dy, LGRAY)
        self.matrix.setPixel(15+dx, 14+dy, LGRAY)

    def lift_right_arm(self, dx, dy):
        dx = self.x_pos + dx
        dy = self.y_pos + dy
        self.matrix.setPixel(15+dx, 9+dy, RED)
        self.matrix.setPixel(16+dx, 9+dy, RED)
        self.matrix.setPixel(17+dx, 9+dy, RED)
        self.matrix.setPixel(18+dx, 9+dy, RED)
        self.matrix.setPixel(19+dx, 9+dy, LGRAY)
        self.matrix.setPixel(120+dx, 9+dy, LGRAY)
