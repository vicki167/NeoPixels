from utils.ColorUtil import *
from utils.matrix import Matrix
from utils.text import *
import utils.numbers as numbers


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

