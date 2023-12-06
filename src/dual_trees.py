# Write your code here :-)
import time
import sys
import math
import board
import neopixel

from random import randint
from utils.ColorUtil import *
from utils.christmas import CandyCane, Stocking

numPix1 = 200

pixels = neopixel.NeoPixel( board.D10, numPix1, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )
pixels2 = neopixel.NeoPixel( board.D0, 100, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )
tree_1 = neopixel.NeoPixel( board.D5, 701, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )
tree_2 = neopixel.NeoPixel( board.D4, 701, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )
led = neopixel.NeoPixel( board.NEOPIXEL, 1, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB )

colors=[RED, WHITE]
tree_cols = [RED, YELLOW, GREEN, PURPLE, DBLUE]
tree_cols_2 = [DBLUE, WHITE, CYAN]
# tree_cols_2 = [CYAN, GREEN, RED]

i = 0
cane = CandyCane(pixels=pixels, start=0, end=199)
#cane2 = CandyCane(pixels=pixels2, start=0, end=199)
tree_rows = []
center_row_num = 6
center_row = []
while True:
    if i == 0:
        cane.stripes(colors, 3)
        pixels2.fill(GREEN)
        pixels2.show()
    #pixels.show()
    for x in range(0, 13):
        tree_1[50*x+1:50*x + 51] = [tree_cols[(i-x)%len(tree_cols)]]*50
        tree_2[50*x+1:50*x + 51] = [tree_cols_2[(i-x)%len(tree_cols_2)]]*50
    tree_1[651:701] = [YELLOW]*50
    tree_1.show()
    # shoot a new color up the center
    tree_2[651:701] = [YELLOW]*50
    tree_2.show()
    #cane2.stripes(colors, 3)
    print(f'Cycle: {i}')
    i += 1
    time.sleep(0.24)
