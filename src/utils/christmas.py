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
        digit_2 = int(days_to_go / 10)
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
                self.rows.append([x, x + 1])
            # the tip of the cane that is one pixel
            self.rows.append([66])
            # now back down, adding to the existing rows
            for x in range(0, 34):
                self.rows[33 - x].append(66 + x)
            self.row_num = len(self.rows)
        elif self.size == 200:
            # four columns of 50 (up, down, up down)
            # self.rows.append([1, 98, 101, 198])
            # self.rows.append([2, 97, 102, 197])
            # self.rows.append([49, 50, 149, 150])
            for x in range(50):
                self.rows.append([0 + x, 99 - x, 100 + x, 199 - x])
            self.row_num = len(self.rows)

    def stripes(self, color_list, width: int):
        i = 0
        j = 0
        for row in self.rows:
            c = color_list[i % len(color_list)]
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
        self.pixels[start: start + 28] = [base_color] * 28
        self.pixels[start + 28: end] = [fringe_color] * 22
        self.pixels.show()


class Train(MatrixDecoration):

    def __init__(self, matrix: Matrix, base_color=DBLUE, accent_color=RED):
        super().__init__(matrix)
        self.base_color = base_color
        self.accent_color = accent_color
        self.wheel_color = BROWN
        self.mw = self.matrix.width
        self.n = 0

    def draw(self, dx=0, dy=0):
        self.matrix.fill(OFF)
        self.draw_caboose(dx, dy)
        self.draw_car(dx, dy)
        self.draw_coal(dx, dy)
        self.draw_engine(dx, dy)
        self.n += 1

    def draw_caboose(self, dx, dy):
        # base rows
        self.matrix.section(x_start=1 + dx, x_end=18 + dx, y_start=0 + dy, y_end=0 + dy, color=self.accent_color)
        self.matrix.section(x_start=2 + dx, x_end=17 + dx, y_start=1 + dy, y_end=1 + dy, color=self.base_color)
        self.matrix.section(x_start=2 + dx, x_end=17 + dx, y_start=5 + dy, y_end=5 + dy, color=self.base_color)
        self.matrix.section(x_start=2 + dx, x_end=18 + dx, y_start=6 + dy, y_end=8 + dy, color=self.base_color)
        self.matrix.section(x_start=5 + dx, x_end=14 + dx, y_start=4 + dy, y_end=4 + dy, color=self.base_color)
        # window verticals
        self.matrix.section(x_start=2 + dx, x_end=2 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=5 + dx, x_end=5 + dx, y_start=2 + dy, y_end=3 + dy, color=self.base_color)
        self.matrix.section(x_start=8 + dx, x_end=8 + dx, y_start=2 + dy, y_end=3 + dy, color=self.base_color)
        self.matrix.section(x_start=11 + dx, x_end=11 + dx, y_start=2 + dy, y_end=3 + dy, color=self.base_color)
        self.matrix.section(x_start=14 + dx, x_end=14 + dx, y_start=2 + dy, y_end=3 + dy, color=self.base_color)
        self.matrix.section(x_start=17 + dx, x_end=17 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        # connector
        self.matrix.setPixel(19 + dx, 7 + dy, self.base_color)
        # end platform
        self.matrix.section(x_start=0 + dx, x_end=0 + dx, y_start=6 + dy, y_end=8 + dy, color=self.accent_color)
        self.matrix.section(x_start=2 + dx, x_end=2 + dx, y_start=7 + dy, y_end=8 + dy, color=self.accent_color)
        self.matrix.setPixel(1 + dx, 8 + dy, self.accent_color)
        # wheels
        self.draw_small_wheel(x=4 + dx, y=8 + dy)
        self.draw_small_wheel(x=7 + dx, y=8 + dy)
        self.draw_small_wheel(x=12 + dx, y=8 + dy)
        self.draw_small_wheel(x=15 + dx, y=8 + dy)

    def draw_car(self, dx, dy):
        # base rows
        self.matrix.section(x_start=20 + dx, x_end=38 + dx, y_start=0 + dy, y_end=0 + dy, color=self.accent_color)
        self.matrix.section(x_start=20 + dx, x_end=38 + dx, y_start=1 + dy, y_end=1 + dy, color=self.base_color)
        self.matrix.section(x_start=20 + dx, x_end=38 + dx, y_start=5 + dy, y_end=8 + dy, color=self.base_color)
        # window verticals
        self.matrix.section(x_start=20 + dx, x_end=20 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=23 + dx, x_end=23 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=26 + dx, x_end=26 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=29 + dx, x_end=29 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=32 + dx, x_end=32 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=35 + dx, x_end=35 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=38 + dx, x_end=38 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        # connector
        self.matrix.setPixel(39 + dx, 7 + dy, self.base_color)
        # wheels
        self.draw_small_wheel(x=22 + dx, y=8 + dy)
        self.draw_small_wheel(x=25 + dx, y=8 + dy)
        self.draw_small_wheel(x=32 + dx, y=8 + dy)
        self.draw_small_wheel(x=35 + dx, y=8 + dy)

    def draw_coal(self, dx, dy):
        # base rows
        self.matrix.section(x_start=40 + dx, x_end=51 + dx, y_start=3 + dy, y_end=8 + dy, color=self.base_color)
        self.matrix.section(x_start=40 + dx, x_end=40 + dx, y_start=3 + dy, y_end=8 + dy, color=self.accent_color)
        self.matrix.section(x_start=51 + dx, x_end=51 + dx, y_start=3 + dy, y_end=8 + dy, color=self.accent_color)
        self.matrix.setPixel(41 + dx, 8 + dy, self.accent_color)
        self.matrix.setPixel(50 + dx, 8 + dy, self.accent_color)
        self.matrix.section(x_start=44 + dx, x_end=47 + dx, y_start=8 + dy, y_end=8 + dy, color=self.accent_color)
        # connector
        self.matrix.setPixel(52 + dx, 7 + dy, self.base_color)
        # wheels
        self.draw_small_wheel(x=42 + dx, y=8 + dy)
        self.draw_small_wheel(x=48 + dx, y=8 + dy)

    def draw_engine(self, dx, dy):
        # main engine body
        self.matrix.section(x_start=56 + dx, x_end=68 + dx, y_start=4 + dy, y_end=8 + dy, color=self.base_color)
        self.matrix.section(x_start=53 + dx, x_end=55 + dx, y_start=5 + dy, y_end=8 + dy, color=self.base_color)
        self.matrix.section(x_start=53 + dx, x_end=58 + dx, y_start=1 + dy, y_end=1 + dy, color=self.base_color)
        self.matrix.section(x_start=53 + dx, x_end=53 + dx, y_start=2 + dy, y_end=4 + dy, color=self.base_color)
        self.matrix.section(x_start=58 + dx, x_end=58 + dx, y_start=2 + dy, y_end=3 + dy, color=self.base_color)
        self.matrix.setPixel(67 + dx, 3 + dy, self.base_color)
        self.matrix.setPixel(68 + dx, 3 + dy, self.base_color)
        # accents
        self.matrix.section(x_start=52 + dx, x_end=59 + dx, y_start=0 + dy, y_end=0 + dy, color=self.accent_color)
        self.matrix.section(x_start=67 + dx, x_end=68 + dx, y_start=1 + dy, y_end=1 + dy, color=self.accent_color)
        self.matrix.section(x_start=66 + dx, x_end=69 + dx, y_start=2 + dy, y_end=2 + dy, color=self.accent_color)
        self.matrix.section(x_start=68 + dx, x_end=69 + dx, y_start=7 + dy, y_end=7 + dy, color=self.accent_color)
        self.matrix.section(x_start=68 + dx, x_end=69 + dx, y_start=7 + dy, y_end=7 + dy, color=self.accent_color)
        self.matrix.section(x_start=68 + dx, x_end=70 + dx, y_start=8 + dy, y_end=8 + dy, color=self.accent_color)
        # connector
        self.matrix.setPixel(52 + dx, 7 + dy, self.base_color)
        # wheels
        # self.matrix.section(x_start=54+dx, x_end=56+dx, y_start=7+dy, y_end=9+dy, color=self.wheel_color)
        self.draw_big_wheel(x=54 + dx, y=7 + dy)
        self.draw_small_wheel(x=59 + dx, y=8 + dy)
        self.draw_small_wheel(x=62 + dx, y=8 + dy)
        self.draw_small_wheel(x=65 + dx, y=8 + dy)

    def draw_small_wheel(self, x, y):
        self.matrix.section(x_start=x, x_end=x + 1, y_start=y, y_end=y + 1, color=self.wheel_color)
        pn = self.n % 4
        if pn == 0:
            self.matrix.setPixel(x + 1, y, TAN)
        elif pn == 1:
            self.matrix.setPixel(x + 1, y + 1, TAN)
        elif pn == 2:
            self.matrix.setPixel(x, y + 1, TAN)
        elif pn == 3:
            self.matrix.setPixel(x, y, TAN)

    def draw_big_wheel(self, x, y):
        self.matrix.section(x_start=x, x_end=x + 2, y_start=y, y_end=y + 2, color=self.wheel_color)
        pn = self.n % 4
        if pn == 0:
            self.matrix.setPixel(x + 2, y, TAN)
        elif pn == 1:
            self.matrix.setPixel(x + 2, y + 2, TAN)
        elif pn == 2:
            self.matrix.setPixel(x, y + 2, TAN)
        elif pn == 3:
            self.matrix.setPixel(x, y, TAN)
