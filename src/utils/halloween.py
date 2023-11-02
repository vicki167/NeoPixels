from .ColorUtil import *


def drawPumpkin(dx, dy, matrix):
    print(f'drawPumpkin')
    #(0-19 is 0)
    PUMPKIN_ORANGE = (240, 120, 0)
    matrix.setPixel(9+dx, 0+dy, GREEN)
    matrix.setPixel(10+dx, 0+dy, GREEN)
    matrix.setPixel(11+dx, 0+dy, GREEN)
    # row
    #(39-20 is 1)
    matrix.setPixel(7+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(8+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(9+dx, 1+dy, GREEN)
    matrix.setPixel(10+dx, 1+dy, GREEN)
    matrix.setPixel(11+dx, 1+dy, GREEN)
    matrix.setPixel(12+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(13+dx, 1+dy, PUMPKIN_ORANGE)
    # row (40-59 is 2)
    for x in range(6,15):
        matrix.setPixel(x+dx, 2+dy, PUMPKIN_ORANGE)
    # row (79-60 is 3)
    for x in range(5,16):
        matrix.setPixel(x+dx, 3+dy, PUMPKIN_ORANGE)
    # row (80-99 is 4)
    for x in range(3,18):
        matrix.setPixel(x+dx, 4+dy, PUMPKIN_ORANGE)
    # row (119-100 is 5)
    for x in range(3, 18):
        matrix.setPixel(x+dx, 5+dy, PUMPKIN_ORANGE)
    # row (120-139 is 6) 22-38, not 26,27,33,34
    for x in range(2, 19):
        matrix.setPixel(x+dx, 6+dy, PUMPKIN_ORANGE)
    # row (159-140 is 7)
    for x in range(2, 19):
        matrix.setPixel(x+dx, 7+dy, PUMPKIN_ORANGE)
    # row (160-179 is 8)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 8+dy, PUMPKIN_ORANGE)
    # row (199-180 is 9)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 9+dy, PUMPKIN_ORANGE)
    # row (200-219 is 10)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 10+dy, PUMPKIN_ORANGE)
    # row (239-220 is 11)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 11+dy, PUMPKIN_ORANGE)
    # row (240-259 is 12)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 12+dy, PUMPKIN_ORANGE)
    # row (279-260 is 13)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 13+dy, PUMPKIN_ORANGE)
    # row (280-299 is 14)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 14+dy, PUMPKIN_ORANGE)
    # row (319-300 is 15)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 15+dy, PUMPKIN_ORANGE)
    # row (320-339 is 16)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 16+dy, PUMPKIN_ORANGE)
    # row (359-340 is 17)
    for x in range(2, 19):
        matrix.setPixel(x+dx, 17+dy, PUMPKIN_ORANGE)
    #  row (360-379 is 18)
    for x in range(3, 18):
        matrix.setPixel(x+dx, 18+dy, PUMPKIN_ORANGE)
    # row (399-380 is 19)
    for x in range(4, 17):
        matrix.setPixel(x+dx, 19+dy, PUMPKIN_ORANGE)
    matrix.show()


def drawJackOLantern(dx, dy, matrix):
    print(f'drawJackOLantern')
    #(0-19 is 0)
    PUMPKIN_ORANGE = (240, 120, 0)
    matrix.setPixel(9+dx, 0+dy, GREEN)
    matrix.setPixel(10+dx, 0+dy, GREEN)
    matrix.setPixel(11+dx, 0+dy, GREEN)
    # row (39-20 is 1)
    matrix.setPixel(7+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(8+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(9+dx, 1+dy, GREEN)
    matrix.setPixel(10+dx, 1+dy, GREEN)
    matrix.setPixel(11+dx, 1+dy, GREEN)
    matrix.setPixel(12+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(13+dx, 1+dy, PUMPKIN_ORANGE)
    # row (40-59 is 2)
    for x in range(5,16):
        matrix.setPixel(x+dx, 2+dy, PUMPKIN_ORANGE)
    # row (79-60 is 3)
    for x in range(4,17):
        matrix.setPixel(x+dx, 3+dy, PUMPKIN_ORANGE)
    # row (80-99 is 4)
    for x in range(3,18):
        matrix.setPixel(x+dx, 4+dy, PUMPKIN_ORANGE)
    # row (119-100 is 5)
    for x in range(3, 18):
        matrix.setPixel(x+dx, 5+dy, PUMPKIN_ORANGE)
    # row (120-139 is 6) 22-38, not 26,27,33,34
    for x in range(2, 19):
        matrix.setPixel(x+dx, 6+dy, PUMPKIN_ORANGE)
    for x in [6,7,13,14]:
        matrix.setPixel(x+dx, 6+dy, OFF)
    # row (159-140 is 7)
    for x in range(2, 19):
        matrix.setPixel(x+dx, 7+dy, PUMPKIN_ORANGE)
    for x in [5,6,7,13,14,15]:
        matrix.setPixel(x+dx, 7+dy, OFF)
    # row (160-179 is 8)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 8+dy, PUMPKIN_ORANGE)
    # row (199-180 is 9)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 9+dy, PUMPKIN_ORANGE)
    # row (200-219 is 10)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 10+dy, PUMPKIN_ORANGE)
    # row (239-220 is 11)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 11+dy, PUMPKIN_ORANGE)
    # row (240-259 is 12)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 12+dy, PUMPKIN_ORANGE)
    for x in [5, 15]:
        matrix.setPixel(x+dx, 12+dy, OFF)
    # row (279-260 is 13)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 13+dy, PUMPKIN_ORANGE)
    for x in [6, 14]:
        matrix.setPixel(x+dx, 13+dy, OFF)
    # row (280-299 is 14)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 14+dy, PUMPKIN_ORANGE)
    for x in range(7, 14):
        matrix.setPixel(x+dx, 14+dy, OFF)
    # row (319-300 is 15)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 15+dy, PUMPKIN_ORANGE)
    for x in range(9, 12):
        matrix.setPixel(x+dx, 15+dy, OFF)
    # row (320-339 is 16)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 16+dy, PUMPKIN_ORANGE)
    # row (359-340 is 17)
    for x in range(2, 19):
        matrix.setPixel(x+dx, 17+dy, PUMPKIN_ORANGE)
    #  row (360-379 is 18)
    for x in range(3, 18):
        matrix.setPixel(x+dx, 18+dy, PUMPKIN_ORANGE)
    # row (399-380 is 19)
    for x in range(4, 17):
        matrix.setPixel(x+dx, 19+dy, PUMPKIN_ORANGE)
    matrix.show()


def drawWinkingJackOLantern(dx, dy, matrix):
    print(f'drawWinkingJackOLantern')
    #(0-19 is 0)
    PUMPKIN_ORANGE = (240, 120, 0)
    matrix.setPixel(9+dx, 0+dy, GREEN)
    matrix.setPixel(10+dx, 0+dy, GREEN)
    matrix.setPixel(11+dx, 0+dy, GREEN)
    # row (39-20 is 1)
    matrix.setPixel(7+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(8+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(9+dx, 1+dy, GREEN)
    matrix.setPixel(10+dx, 1+dy, GREEN)
    matrix.setPixel(11+dx, 1+dy, GREEN)
    matrix.setPixel(12+dx, 1+dy, PUMPKIN_ORANGE)
    matrix.setPixel(13+dx, 1+dy, PUMPKIN_ORANGE)
    # row (40-59 is 2)
    for x in range(5,16):
        matrix.setPixel(x+dx, 2+dy, PUMPKIN_ORANGE)
    # row (79-60 is 3)
    for x in range(4,17):
        matrix.setPixel(x+dx, 3+dy, PUMPKIN_ORANGE)
    # row (80-99 is 4)
    for x in range(3,18):
        matrix.setPixel(x+dx, 4+dy, PUMPKIN_ORANGE)
    # row (119-100 is 5)
    for x in range(3, 18):
        matrix.setPixel(x+dx, 5+dy, PUMPKIN_ORANGE)
    # row (120-139 is 6) 22-38, not 26,27,33,34
    for x in range(2, 19):
        matrix.setPixel(x+dx, 6+dy, PUMPKIN_ORANGE)
    for x in [6,7]:
        matrix.setPixel(x+dx, 6+dy, OFF)
    # row (159-140 is 7)
    for x in range(2, 19):
        matrix.setPixel(x+dx, 7+dy, PUMPKIN_ORANGE)
    for x in [5,6,7]:
        matrix.setPixel(x+dx, 7+dy, OFF)
    # row (160-179 is 8)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 8+dy, PUMPKIN_ORANGE)
    # row (199-180 is 9)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 9+dy, PUMPKIN_ORANGE)
    # row (200-219 is 10)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 10+dy, PUMPKIN_ORANGE)
    # row (239-220 is 11)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 11+dy, PUMPKIN_ORANGE)
    # row (240-259 is 12)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 12+dy, PUMPKIN_ORANGE)
    for x in [5, 15]:
        matrix.setPixel(x+dx, 12+dy, OFF)
    # row (279-260 is 13)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 13+dy, PUMPKIN_ORANGE)
    for x in [6, 14]:
        matrix.setPixel(x+dx, 13+dy, OFF)
    # row (280-299 is 14)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 14+dy, PUMPKIN_ORANGE)
    for x in range(7, 14):
        matrix.setPixel(x+dx, 14+dy, OFF)
    # row (319-300 is 15)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 15+dy, PUMPKIN_ORANGE)
    for x in range(9, 12):
        matrix.setPixel(x+dx, 15+dy, OFF)
    # row (320-339 is 16)
    for x in range(1, 20):
        matrix.setPixel(x+dx, 16+dy, PUMPKIN_ORANGE)
    # row (359-340 is 17)
    for x in range(2, 19):
        matrix.setPixel(x+dx, 17+dy, PUMPKIN_ORANGE)
    #  row (360-379 is 18)
    for x in range(3, 18):
        matrix.setPixel(x+dx, 18+dy, PUMPKIN_ORANGE)
    # row (399-380 is 19)
    for x in range(4, 17):
        matrix.setPixel(x+dx, 19+dy, PUMPKIN_ORANGE)
    matrix.show()


def drawGhost(dx, dy, color, matrix):
    print(f'drawGhost')
    # do the below since this was originally drawn in the middle of a 20X20
    dx = dx - 5
    dy = dy - 2
    # 9-13,2
    for i in range(9,14):
        matrix.setPixel(i+dx,2+dy, color)
    # 8-14,3
    for i in range(8,15):
        matrix.setPixel(i+dx,3+dy, color)
    # 7-15,4
    for i in range(7,16):
        matrix.setPixel(i+dx,4+dy, color)
    # 6-7-10-11-12-15-16,5
    xPos = [6,7,10,11,12,15,16]
    for i in xPos:
        matrix.setPixel(i+dx,5+dy,color)
    # 6-7-10-11-12-15-16,6
    for i in xPos:
        matrix.setPixel(i+dx,6+dy,color)
    # 5-17,7
    for j in range(7,16):
        for i in range(5,17):
            matrix.setPixel(i+dx,j+dy, color)
    # 5-6|8-9|11|13-14|16-17,16
    matrix.setPixel(5+dx,16+dy,color)
    matrix.setPixel(6+dx,16+dy,color)
    matrix.setPixel(8+dx,16+dy,color)
    matrix.setPixel(9+dx,16+dy,color)
    matrix.setPixel(11+dx,16+dy,color)
    matrix.setPixel(13+dx,16+dy,color)
    matrix.setPixel(14+dx,16+dy,color)
    matrix.setPixel(16+dx,16+dy,color)
    # 5-6|8-9|11|13-14|16-17,17
    matrix.setPixel(5+dx,17+dy,color)
    matrix.setPixel(6+dx,17+dy,color)
    matrix.setPixel(8+dx,17+dy,color)
    matrix.setPixel(9+dx,17+dy,color)
    matrix.setPixel(11+dx,17+dy,color)
    matrix.setPixel(13+dx,17+dy,color)
    matrix.setPixel(14+dx,17+dy,color)
    matrix.setPixel(16+dx,17+dy,color)
    #setPixel(17+dx,17+dy,color)
    # 5|8|11|14|17,18
    matrix.setPixel(5+dx,18+dy,color)
    matrix.setPixel(8+dx,18+dy,color)
    matrix.setPixel(11+dx,18+dy,color)
    matrix.setPixel(14+dx,18+dy,color)
    matrix.setPixel(16+dx,18+dy,color)
    # eyes
    # 8,6
    matrix.setPixel(8+dx,6+dy,RED)
    # 13,6
    matrix.setPixel(13+dx,6+dy,RED)
    matrix.show()
