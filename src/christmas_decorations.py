# Write your code here :-)
import time
import sys
import math
import board
import neopixel

from random import randint
from utils.ColorUtil import *
from utils.christmas import CandyCane, Stocking

numPix1 = 150

pixels = neopixel.NeoPixel( board.D27, numPix1, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB )
led = neopixel.NeoPixel( board.NEOPIXEL, 1, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB )

colors=[RED, WHITE]
sc=[RED, GREEN, DBLUE]

i = 0
cane = CandyCane(pixels=pixels, start=0, end=99)
while True:
    print(f'Cycle: {i}')
    cane.stripes(colors, 2)
    stocking = Stocking(pixels=pixels, start=100, end=150, base_color=RED, fringe_color=WHITE)
    i += 1
    time.sleep(0.2)
