# Write your code here :-)
__author__ = 'john'

import random
import time
import board
import neopixel

width = 20
height = 20
numPix = 800
pixels = neopixel.NeoPixel(board.D27, numPix, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB)

RED = (255, 0, 0)
YELLOW = (255, 255, 0)
GOLD = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
H_CYAN = (0, 130, 130)
BLUE = (0, 0, 102)
DBLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
ORANGE = (255, 60, 0)
# ORANGE = (255, 85, 0)
GREEN1 = (0, 125, 0)
ORANGE1 = (255, 50, 0)
BULB_WHITE = (255, 150, 45)

colors = [RED, YELLOW, GREEN, DBLUE, WHITE]
xmasColors = [RED, WHITE, GREEN]
peppermintColors = [RED, GREEN]
winterColors = [DBLUE, BLUE, H_CYAN, CYAN, WHITE]
treeColors = winterColors

count = 0


def draw_bell(bell_pixels, color, counter, offset):
    delay = 0
    # top
    bell_pixels[160 + offset:165 + offset] = [color] * 5
    if counter == 0:
        bell_pixels[48 + offset:97 + offset] = [color] * 49
        bell_pixels[147 + offset] = color
        bell_pixels[183 + offset] = color
        bell_pixels[40 + offset:46 + offset] = [color] * 6
        # bell_pixels.show()
        counter = 1
        delay = 0.65
    elif count == 1:
        bell_pixels[97 + offset:145 + offset] = [color] * 48
        bell_pixels[181 + offset] = color
        bell_pixels[154 + offset] = color
        bell_pixels[184 + offset] = color
        bell_pixels[40 + offset:47 + offset] = [color] * 7
        # bell_pixels.show()
        delay = 0.7
        counter = 2
    elif count == 2:
        bell_pixels[145 + offset:200 + offset] = [color] * 55
        bell_pixels[150 + offset] = OFF
        bell_pixels[41 + offset:48 + offset] = [color] * 7
        # bell_pixels.show()
        delay = 0.65
        counter = 3
    elif count == 3:
        bell_pixels[97 + offset:145 + offset] = [color] * 48
        bell_pixels[181 + offset] = color
        bell_pixels[154 + offset] = color
        bell_pixels[184 + offset] = color
        bell_pixels[40 + offset:47 + offset] = [color] * 7
        delay = 0.7
        # bell_pixels.show()
        counter = 0
    return counter, delay


while True:
    print("Cycle -", count)
    pixels.fill(OFF)
    pixels.show()

    color = GOLD
    color = 0xFF0000
    draw_bell(pixels, color, count, 0)
    draw_bell(pixels, color, count, 200)
    draw_bell(pixels, color, count, 400)
    count, delay = draw_bell(pixels, color, count, 600)
    pixels.show()
    time.sleep(delay)
