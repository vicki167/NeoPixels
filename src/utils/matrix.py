# Write your code here :-)
__author__ = 'john'

# import neopixel
from .ColorUtil import *

UPPER_LEFT = 0
UPPER_RIGHT = 1
LOWER_LEFT = 2
LOWER_RIGHT = 3


class Matrix:

    def __init__(self, width, height, pin, brightness=0.2, auto_write=False, pixel_order=None,
                 origin=UPPER_LEFT, offset=1, vertical=True):
        self.width = width
        self.height = height
        self.offset = offset
        self.numPix = width * height + offset
        self.origin = origin
        self.vertical = vertical
        # if check is necessary so that we can test without running on a board
        if pin:
            import neopixel
            if not pixel_order:
                pixel_order = neopixel.RGB
            self.pixels = neopixel.NeoPixel(pin, self.numPix, brightness=brightness, auto_write=auto_write,
                                            pixel_order=pixel_order)
            self.pixels.fill(OFF)
            self.pixels.show()

    def baseSetPixel(self, x, y, color, flip=False):
        # convert the x and y to a pixel position
        if flip:
            x = self.height - x - 1  # subract one since zero
        if y % 2 == 0:  # even rows
            p = x + y * self.width  # even rows
        else:  # odd rows (count back from the right)
            p = (self.width - x - 1) + y * self.width
        p += self.offset
        # set the pixel color, making sure that we do not write over the pixel limit
        if p < self.numPix:
            # print(p)
            self.pixels[p] = color

    def get_pix_num(self, x, y, swap_x=False, swap_y=False):
        p = 0
        if swap_x and swap_y:
            x = self.height - x - 1  # subtract one since zero
            y = self.width - y - 1  # subtract one since zero
        elif swap_x:
            x = self.width - x - 1  # swap X about Y axis
        elif swap_y:
            y = self.height - y - 1  # swap Y about x axis
        # use height as the factor if the lights are vertical, width if horizontal
        factor = self.height if self.vertical else self.width
        # convert the x and y to a pixel position
        if y % 2 == 0:  # even rows
            p = x + y * factor
        else:  # odd rows (count back from the right)
            p = (factor - x - 1) + y * factor
        return p

    def compute_pixel(self, x, y):
        p = 0
        if self.origin == UPPER_LEFT:
            p = self.get_pix_num(y, x) if self.vertical else self.get_pix_num(x, y)
            # p = self.get_pix_num(y, x)
        elif self.origin == LOWER_LEFT:
            p = self.get_pix_num(y, x, swap_x=True)
        elif self.origin == LOWER_RIGHT:
            p = self.get_pix_num(y, x, swap_x=True, swap_y=True)
            # self.baseSetPixel_lr(x,y,color)
        elif self.origin == UPPER_RIGHT:
            p = self.get_pix_num(x, y, swap_x=True)
        else:
            print('NOT IMPLEMENTED!!')
        # add the offset
        p += self.offset
        return p

    def setPix_working(self, x, y, color, swap_x=False, swap_y=False):
        p = 0
        if swap_x and swap_y:
            x = self.height - x - 1  # subract one since zero
            y = self.width - y - 1  # subract one since zero
        elif swap_x:
            x = self.width - x - 1  # swap X about Y axis
        elif swap_y:
            y = self.height - y - 1  # swap Y about x axis
        # use height as the factor if the lights are vertical, width if horizontal
        factor = self.height if self.vertical else self.width
        # convert the x and y to a pixel position
        if y % 2 == 0:  # even rows
            p = x + y * factor
        else:  # odd rows (count back from the right)
            p = (factor - x - 1) + y * factor
        return p

    def setPixel(self, x, y, color):
        # verify the x and y positions are within the bounds of the matrix
        if x >= self.width or x < 0:
            print(f'{x} must be between 0 and {self.width}')
            return
        if y >= self.height or y < 0:
            print(f'{x} must be between 0 and {self.width}')
            return
        p = self.compute_pixel(x, y)
        # set the pixel color, making sure that we do not write over the pixel limit
        if p < self.numPix:
            # print(p)
            self.pixels[p] = color

    def setRawPixel(self, pos, color):
        if pos < self.numPix:
            # print(p)
            self.pixels[pos] = color

    def fill(self, color, show=False):
        self.pixels.fill(color)
        if show:
            self.show()

    def show(self):
        self.pixels.show()


# Helper to give us a nice color swirl
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0):
        return [0, 0, 0]
    if (pos > 255):
        return [0, 0, 0]
    if (pos < 85):
        return [int(pos * 3), int(255 - (pos * 3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos * 3), 0, int(pos * 3)]
    else:
        pos -= 170
        return [0, int(pos * 3), int(255 - pos * 3)]
