# Write your code here :-)
__author__ = 'john'

import random
import time
import board
import neopixel
from utils.ColorUtil import *
from utils.matrix import Matrix, UPPER_LEFT

def drawGhost(dx, dy, color, pixels):
    dx = dx - 5
    dy = dy - 2
    # 9-13,2
    for i in range(9,14):
        pixels.setPixel(i+dx,2+dy, color)
    # 8-14,3
    for i in range(8,15):
        pixels.setPixel(i+dx,3+dy, color)
    # 7-15,4
    for i in range(7,16):
        pixels.setPixel(i+dx,4+dy, color)
    # 6-7-10-11-12-15-16,5
    xPos = [6,7,10,11,12,15,16]
    for i in xPos:
        pixels.setPixel(i+dx,5+dy,color)
    # 6-7-10-11-12-15-16,6
    for i in xPos:
        pixels.setPixel(i+dx,6+dy,color)
    # 5-17,7
    for j in range(7,16):
        for i in range(5,17):
            pixels.setPixel(i+dx,j+dy, color)
    # 5-6|8-9|11|13-14|16-17,16
    pixels.setPixel(5+dx,16+dy,color)
    pixels.setPixel(6+dx,16+dy,color)
    pixels.setPixel(8+dx,16+dy,color)
    pixels.setPixel(9+dx,16+dy,color)
    pixels.setPixel(11+dx,16+dy,color)
    pixels.setPixel(13+dx,16+dy,color)
    pixels.setPixel(14+dx,16+dy,color)
    pixels.setPixel(16+dx,16+dy,color)
    # 5-6|8-9|11|13-14|16-17,17
    pixels.setPixel(5+dx,17+dy,color)
    pixels.setPixel(6+dx,17+dy,color)
    pixels.setPixel(8+dx,17+dy,color)
    pixels.setPixel(9+dx,17+dy,color)
    pixels.setPixel(11+dx,17+dy,color)
    pixels.setPixel(13+dx,17+dy,color)
    pixels.setPixel(14+dx,17+dy,color)
    pixels.setPixel(16+dx,17+dy,color)
    #setPixel(17+dx,17+dy,color)
    # 5|8|11|14|17,18
    pixels.setPixel(5+dx,18+dy,color)
    pixels.setPixel(8+dx,18+dy,color)
    pixels.setPixel(11+dx,18+dy,color)
    pixels.setPixel(14+dx,18+dy,color)
    pixels.setPixel(16+dx,18+dy,color)
    # eyes
    # 8,6
    pixels.setPixel(8+dx,6+dy,YELLOW)
    # 13,6
    pixels.setPixel(13+dx,6+dy,YELLOW)
    pixels.show()

ghost_color = WHITE
ghost_color = DBLUE
matrix = None
count = 0
while True:
    if (count == 0 ):
        matrix = Matrix(width=20, height=20, pin=board.A3, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB, origin=UPPER_LEFT)
        matrix.fill( OFF )
        matrix.show()
    print("Cycle -", count)

    # have a ghost rise out of the ground, then float to the side, then fade out
    # rise up
    for i in range(20):
        matrix.fill( OFF )
        drawGhost( 0, 19-i, ghost_color, matrix)
        time.sleep( 0.2 )

    # todo - create larger offsets for 4X8
    offsets = [r for r in range(0,9)]
    last_y = 0
    for i in offsets:
        matrix.fill( OFF )
        drawGhost( i, 0, ghost_color, matrix )
        last_y = i
        #pixels.show()
        time.sleep( 0.2 )
    time.sleep(1)

    # fade out
    col = ghost_color
    for i in range(20):
        col = (col[0] / 2, col[1] / 2, col[2] / 2)
        drawGhost( last_y, 0, col, matrix )
        time.sleep( 0.2 )


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
