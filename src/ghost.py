# Write your code here :-)
__author__ = 'john'

import random
import time
import board
import neopixel
from utils.ColorUtil import *
from utils.matrix import Matrix, UPPER_LEFT, LOWER_LEFT
from utils.halloween import *


ghost_color = WHITE
#ghost_color = DBLUE
matrix = None
pumpkin_matrix = None
rip = neopixel.NeoPixel( board.D9, 100, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB )

count = 0
while True:
    if (count == 0 ):
        matrix = Matrix(width=40, height=20, pin=board.D0, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB, origin=UPPER_LEFT)
        matrix.fill( OFF )
        matrix.show()
        pumpkin_matrix = Matrix(width=20, height=20, pin=board.D10, brightness=0.10, auto_write=False, pixel_order=neopixel.RGB, origin=LOWER_LEFT)
        pumpkin_matrix.fill( OFF )
        # draw pumpkin
        drawJackOLantern(0,0, pumpkin_matrix)
        #pumpkin_matrix.fill(RED)
        pumpkin_matrix.show()
        led = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.4)
        led[0] = DBLUE
        rip.fill(0x7b5d92)
        rip.show()
    print("Cycle -", count)

    # have a ghost rise out of the ground, then float to the side, then fade out
    # rise up
    offsets = [r for r in range(0,29)]
    start_pos = 0
    r = random.randint(0, 2)
    factor = 1
    print(r)
    if r % 2 == 1:
        print('reverse')
        factor = -1
        start_pos = 29
    for i in range(20):
        matrix.fill( OFF )
        drawGhost( start_pos, 19-i, ghost_color, matrix)
        time.sleep( 0.11 )

    pumpkin_matrix.fill(OFF)
    drawWinkingJackOLantern(0, 0, pumpkin_matrix)
    time.sleep(0.4)
    drawJackOLantern(0,0, pumpkin_matrix)

    # todo - create larger offsets for 4X8
    last_y = 0
    for i in offsets:
        matrix.fill( OFF )
        last_y = start_pos + i*factor
        drawGhost( last_y, 0, ghost_color, matrix )
        # pixels.show()
        time.sleep( 0.11 )
    time.sleep(1)

    # fade out
    col = ghost_color
    for i in range(20):
        col = (col[0] / 2, col[1] / 2, col[2] / 2)
        drawGhost( last_y, 0, col, matrix )
        time.sleep( 0.22 )

    pumpkin_matrix.fill(OFF)
    drawWinkingJackOLantern(0, 0, pumpkin_matrix)
    time.sleep(0.4)
    drawJackOLantern(0,0, pumpkin_matrix)


    if False:
        for y in range(width):
            for x in range(width):
                matrix.fill( OFF )
                setPixel(x, y, ghost_color)
                matrix.show()
                time.sleep(0.01)
    matrix.show()

    time.sleep( 0.1 )
    count += 1
