# Write your code here :-)
import time
import sys
import math
import board
import neopixel

from random import randint
from utils.ColorUtil import *
from utils.christmas import CandyCane

numPix1 = 256

pixels = neopixel.NeoPixel( board.D27, numPix1, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )
led = neopixel.NeoPixel( board.NEOPIXEL, 1, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )

colors=[RED, GREEN]

i = 0
while True:
    print(f'Cycle: {i}')
    cane = CandyCane(pixels=pixels, start=0, end=99)
    cane.fill(RED)
    i += 1
    time.sleep(1)
