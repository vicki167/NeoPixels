# CircuitPython demo - NeoPixel
import time
import sys
import math

import board
import neopixel

from random import randint

from adafruit_circuitplayground import cp

cp.pixels.auto_write = False
cp.pixels.brightness = 0.05

RED = (255, 0, 0)
YELLOW = 0xFED800
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
H_CYAN = (0, 130, 130)
BLUE = (0, 0, 102)
DBLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
ORANGE = (160, 60, 0)
GREEN1 = (0, 125, 0)
ORANGE1 = (255, 50, 0)
BULB_WHITE = (255, 150, 45)

colors = [DBLUE, CYAN]
colors = [ORANGE, GREEN, WHITE]
xmasColors = [RED, GREEN, WHITE]

numPix = 150
numPix = 100

pixel_pin = board.A3

pixels = neopixel.NeoPixel( pixel_pin, numPix, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB )

delay = 0.5
i = 0

def init():
    print( "> init" )

def sparkle( color = DBLUE ):
    pixels.fill( color )
    pixels.write()
    x = 3
    for n in range( 3000 ):
        pixels[x] = color
        x = randint(0, numPix - 1)
        pixels[x] = WHITE
        pixels.write()

def reset():
    pixels.fill( OFF )
    pixels.write()

n = 0
while True:
    if i == 0:
        init()
    print( 'Cycle ', i )

    #cp.pixels.fill( BLUE if i % 2 == 0 else CYAN )
    cols = colors
    pixels[0:50] = cols[i%len(cols)]*50
    pixels[50:80] = cols[(i+1)%len(cols)]*30
    pixels[80:100] = cols[(i+2)%len(cols)]*20
    if False:
        for x in range(numPix):
            pixels[x] = cols[(x-i)%len(cols)]
        for x in range(10):
            cp.pixels[x] = cols[(i)%len(cols)]
    # turn 1/4 off
    #pixels.fill( colors[i%len(colors)] )
    cp.pixels.show()
    pixels.show()
    i += 1
    time.sleep( delay )

