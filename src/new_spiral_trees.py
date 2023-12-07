# Write your code here :-)
import time
import sys
import math
import board
import neopixel

from random import randint
from utils.ColorUtil import *
from utils.matrix import Matrix, LOWER_RIGHT
from utils.trees import FireworkTree, SpiralTree

PINK = (255, 150, 200)
colors = [RED, YELLOW, GREEN, DBLUE, PURPLE]

matrix = Matrix(width=19, height=20, pin=board.D52, brightness=0.15, auto_write=False, offset=0,
                pixel_order=neopixel.RGB, extra_pixels=20, origin=LOWER_RIGHT)
spiral = SpiralTree(matrix)

while True:
    print(f'Cycle {i}')
    spiral.execute(top_color=WHITE, bottom_color=GREEN, offset=i)
    #matrix.setRawPixels(700, 800, YELLOW)
    matrix.setRawPixels(320, 400, YELLOW)
    i += 1
    # time.sleep(0.2)
