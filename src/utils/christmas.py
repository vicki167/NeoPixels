import numbers

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
        d(24, 2, self.tc)
        a(29, 2, self.tc)
        y(33, 2, self.tc)
        s(37, 2, self.tc)
        #  till
        t(26, 8, self.tc)
        i(30, 8, self.tc)
        l(32, 8, self.tc)
        l(36, 8, self.tc)
        #  Christmas
        c(3, 15, self.tc)
        h(7, 16, self.tc)
        r(11, 15, self.tc)
        i(15, 15, self.tc)
        s(17, 15, self.tc)
        t(21, 15, self.tc)
        m(25, 15, self.tc)
        a(31, 15, self.tc)
        s(35, 15, self.tc)
        bang(39, 15, self.tc)

    def set_days(self, days_to_go: int):
        # get 100s place
        digits = [int(days_to_go / 100)]
        # get 10s place
        digit_2 = int(days_to_go/10)
        if digit_2 > 9:
            digit_2 = digit_2 % 10
        digits.append(digit_2)
        # get 1s place
        digits.append(days_to_go % 10)
        # draw each digit
        digit_width = 8
        for idx, digit in digits:
            self._get_method(digit)(digit_width * idx, 0, self.nc, self.matrix)

    def _get_method(self, n: int):
        return getattr(numbers, f'_{n}')

