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
fgColors = [RED, ORANGE1, YELLOW, CYAN, PURPLE]
colors = [RED, ORANGE1, YELLOW, GREEN, DBLUE, PURPLE]
colors = [RED, YELLOW, GREEN, DBLUE, PURPLE]
xmasColors = [DBLUE]
# xmasColors = [RED, GREEN]
winterColors = [DBLUE]
vdayColors = [RED]
ukColors = [BLUE]
irishColors = [YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, WHITE, WHITE, WHITE, YELLOW, YELLOW, YELLOW, YELLOW,
               YELLOW, YELLOW, ORANGE, ORANGE, ORANGE]
easter = [YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, YELLOW, PURPLE, PURPLE, PURPLE, YELLOW, YELLOW, YELLOW, YELLOW,
          YELLOW, YELLOW, CYAN, CYAN, CYAN]

numPix1 = 700

# tree2 = neopixel.NeoPixel( board.A5, numPix1, brightness=0.3, auto_write=False, pixel_order=neopixel.RGB )
tree1 = neopixel.NeoPixel(board.D33, numPix1, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB)
# pixels = neopixel.NeoPixel( board.D52, 400, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB )

i = 0
j = 0
k = 6
d = 3
e = 9
bgCol = OFF
cols = [RED, PURPLE, DBLUE, CYAN, GREEN, YELLOW]
while False:
    if i == 0:
        tree1.fill(OFF)
        # tree2.fill( OFF )
        tree1.show()
        # tree2.show()
    n = 0
    m = 0
    for x in range(0, 17):
        col1 = OFF
        col2 = OFF
        if x % 2 == 0:
            col1 = cols[(x + i) % len(cols)]
            col2 = cols[(x + i) % len(cols)]
            # col1 = cols[ (x) % len(cols) ]
            # col2 = cols[ (x) % len(cols) ]
            n = x * 50 + 2
            m = n + 48
        else:
            col1 = cols[(x + i) % len(cols)]
            col2 = cols[(x + i) % len(cols)]
            # col1 = cols[ (x) % len(cols) ]
            # col2 = cols[ (x) % len(cols) ]
            n = 50 * x
            m = n + 48
        # if x == j or x == k:
        # col1 = WHITE
        # col2 = WHITE
        # if x == d or x == e:
        # col1 = WHITE
        # col2 = WHITE
        # tree1[n:m] = [col1] * 60
        tree1[n:m] = [col2] * 48
    # add start at top
    tree1[850:900] = [YELLOW] * 50

    # minor corrections due to differences in where anchored
    # tree1[45] = OFF
    # tree1[154] = OFF
    # tree1[245] = OFF

    tree1.show()
    # tree2.show()
    print("Cycle - ", i)
    i += 1
    j = (j + 1) % 17
    k = (k + 1) % 17
    d = (d + 1) % 17
    e = (e + 1) % 17
    time.sleep(0.33)

while False:
    tree1[0:650] = [DBLUE] * 650
    tree1[650:700] = [YELLOW] * 50
    tree1.show()
    print(f'Cycle {i}')
    i += 1
    time.sleep(1)

matrix = Matrix(width=19, height=20, pin=board.D52, brightness=0.15, auto_write=False, offset=0,
                pixel_order=neopixel.RGB, origin=LOWER_RIGHT)
spiral = SpiralTree(matrix)

while True:
    print(f'Cycle {i}')
    spiral.execute(offset=i)
    i += 1
    # time.sleep(0.2)

# setup strands
# tree1Strands = [tree1[38:100]]
# tree1Strands.append(tree1[100:162])
# tree1Strands.append(tree1[238:300])
# tree1Strands.append(tree1[300:362])
# tree1Strands.append(tree1[438:500])
# tree1Strands.append(tree1[500:562])
# tree1Strands.append(tree1[638:700])
# tree1Strands.append(tree1[700:762])
# tree1Strands.append(tree1[838:900])
# tree1Strands.append(tree1[900:962])
# tree1Strands.append(tree1[1038:1100])
# tree1Strands.append(tree1[1100:1162])
#
# tree2Strands = [tree2[38:100]]
# tree2Strands.append(tree2[100:162])
# tree2Strands.append(tree2[238:300])
# tree2Strands.append(tree2[300:362])
# tree2Strands.append(tree2[438:500])
# tree2Strands.append(tree2[500:562])
# tree2Strands.append(tree2[638:700])
# tree2Strands.append(tree2[700:762])
# tree2Strands.append(tree2[838:900])
# tree2Strands.append(tree2[900:962])
# tree2Strands.append(tree2[1038:1100])
# tree2Strands.append(tree2[1100:1162])
