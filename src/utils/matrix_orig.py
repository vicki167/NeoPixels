# Write your code here :-)
__author__ = 'john'

import random
import time
import board
import neopixel
from .ColorUtil import *

UPPER_LEFT = 0
UPPER_RIGHT = 1
LOWER_LEFT = 2
LOWER_RIGHT = 3

class Matrix:

    def __init__(self, width, height, pin, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB, origin=UPPER_LEFT, offset=1):
        self.width = width
        self.height = height
        self.offset = offset
        self.numPix = width * height + offset
        self.origin = origin
        self.pixels = neopixel.NeoPixel(pin, self.numPix, brightness=brightness, auto_write=auto_write, pixel_order=pixel_order)
        self.pixels.fill(OFF)
        self.pixels.show()

    def baseSetPixel(self, x, y, color, flip=False):
        # convert the x and y to a pixel position
        if flip:
            x = self.height - x - 1 # subract one since zero
        if y % 2 == 0:   # even rows
            p = x + y * self.width # even rows
        else:         # odd rows (count back from the right)
            p = (self.width - x - 1) + y * self.width
        p += self.offset
        # set the pixel color, making sure that we do not write over the pixel limit
        if p < self.numPix:
            #print(p)
            self.pixels[p] = color

    def setPixel(self, x, y, color):
        if self.origin == UPPER_LEFT:
            self.baseSetPixel(x, y, color)
        elif self.origin == LOWER_LEFT:
            self.baseSetPixel(y, x, color, flip=True)
        else:
            print('NOT IMPLEMENTED!!')

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
        return [int(pos * 3), int(255 - (pos*3)), 0]
    elif (pos < 170):
        pos -= 85
        return [int(255 - pos*3), 0, int(pos*3)]
    else:
        pos -= 170
        return [0, int(pos*3), int(255 - pos*3)]
