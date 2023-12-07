from utils.ColorUtil import *
from utils.matrix import Matrix


class Menorah:

    def __init__(self, matrix: Matrix):
        self.matrix = matrix
        self._draw_base()
        self._draw_shamash()

    def _draw_base(self):
        for x in range(3, 37):
            self.matrix.setPixel(x, 15, GOLD)
            self.matrix.setPixel(x, 16, GOLD)
        for x in [3, 4, 7, 8, 11, 12, 15, 16, 19, 20, 23, 24, 27, 28, 31, 32, 35, 36]:
            self.matrix.setPixel(x, 14, GOLD)
        for x in [19, 20]:
            self.matrix.setPixel(x, 13, GOLD)
            self.matrix.setPixel(x, 17, GOLD)
            self.matrix.setPixel(x, 18, GOLD)
            self.matrix.setPixel(x, 19, GOLD)
        for x in [17, 18, 21, 22]:
            self.matrix.setPixel(x, 19, GOLD)
        self.matrix.setPixel(18, 13, GOLD)
        self.matrix.setPixel(21, 13, GOLD)
        self.show()

    def _draw_shamash(self, day: int):
        self._draw_candle(19, 1)
        self._draw_flame(19, 1)

    def _draw_candle(self, x_off: int, y_off: int):
        for y in range(3, 12):
            self.matrix.setPixel(x_off, y + y_off, DBLUE)
            self.matrix.setPixel(x_off + 1, y + y_off, DBLUE)

    def _draw_flame(self, x_off: int, y_off: int, left: bool = True):
        tip_offset = 0 if left else 1
        self.matrix.setPixel(x_off + tip_offset, y_off, YELLOW)
        self.matrix.setPixel(x_off + 1, y_off + 1, YELLOW)
        self.matrix.setPixel(x_off + 1, y_off + 2, YELLOW)
        self.matrix.setPixel(x_off + tip_offset, y_off + 2, ORANGE)

    def set_day(self, day: int):
        if day == 1:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
        elif day == 2:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(35, 2)
        elif day == 3:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(31, 2)
            self._draw_candle(27, 2)
            self._draw_flame(27, 2)
        elif day == 4:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(31, 2)
            self._draw_candle(27, 2)
            self._draw_flame(27, 2)
            self._draw_candle(23, 2)
            self._draw_flame(23, 2)
        elif day == 5:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(31, 2)
            self._draw_candle(27, 2)
            self._draw_flame(27, 2)
            self._draw_candle(23, 2)
            self._draw_flame(23, 2)
            self._draw_candle(15, 2)
            self._draw_flame(15, 2)
        elif day == 6:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(31, 2)
            self._draw_candle(27, 2)
            self._draw_flame(27, 2)
            self._draw_candle(23, 2)
            self._draw_flame(23, 2)
            self._draw_candle(15, 2)
            self._draw_flame(15, 2)
            self._draw_candle(11, 2)
            self._draw_flame(11, 2)
        elif day == 6:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(31, 2)
            self._draw_candle(27, 2)
            self._draw_flame(27, 2)
            self._draw_candle(23, 2)
            self._draw_flame(23, 2)
            self._draw_candle(15, 2)
            self._draw_flame(15, 2)
            self._draw_candle(11, 2)
            self._draw_flame(11, 2)
            self._draw_candle(7, 2)
            self._draw_flame(7, 2)
        else:
            self._draw_candle(35, 2)
            self._draw_flame(35, 2)
            self._draw_candle(31, 2)
            self._draw_flame(31, 2)
            self._draw_candle(27, 2)
            self._draw_flame(27, 2)
            self._draw_candle(23, 2)
            self._draw_flame(23, 2)
            self._draw_candle(15, 2)
            self._draw_flame(15, 2)
            self._draw_candle(11, 2)
            self._draw_flame(11, 2)
            self._draw_candle(7, 2)
            self._draw_flame(7, 2)
            self._draw_candle(3, 2)
            self._draw_flame(3, 2)
