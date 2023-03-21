__author__ = 'john'

import random
import time
import board
import neopixel
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi
from DisplayUtil import *

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise

print("ESP32 SPI webclient test")

JSON_URL = "http://worldtimeapi.org/api/timezone/America/New_York"
JSON_URL = "http://192.168.178.116:8000/api/day"
JSON_URL = "https://d6u9xjk595.execute-api.us-east-1.amazonaws.com/api/day"

# If you are using a board with pre-defined ESP32 Pins:
esp32_cs = DigitalInOut(board.ESP_CS)
esp32_ready = DigitalInOut(board.ESP_BUSY)
esp32_reset = DigitalInOut(board.ESP_RESET)

spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
esp = adafruit_esp32spi.ESP_SPIcontrol(spi, esp32_cs, esp32_ready, esp32_reset)

requests.set_socket(socket, esp)

print("Connecting to AP...")
counter = 0
while not esp.is_connected:
    try:
        esp.connect_AP(secrets["ssid"], secrets["password"])
    except Exception as e:
        counter += 1
        print(f"could not connect to AP, retrying {counter}: ", e)
        if counter == 60:
            break
        continue
print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)
print("My IP address is", esp.pretty_ip(esp.ip_address))
print("Attempting connection to: ", JSON_URL)
curDay = 359
counter = 0
errorFlag = False
notFound = True
while counter < 3 and notFound:
    try:
        r = requests.get( JSON_URL )
        js = r.json()
        print(js)
        curDay = js["day_of_year"]
        daysToGo = js["days_to_christmas"]
        notFound = False
    except Exception as e:
        print(f"Error querying the time server {counter}: ", e)
        time.sleep(0.5)
        counter += 1
        if counter == 3:
            errorFlag = True
            break
        continue

print('Current day: ', curDay)
width = 20
height = 40
numPix = 800
pixels = neopixel.NeoPixel(board.A5, numPix, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB)
pixels2 = neopixel.NeoPixel(board.A0, 400, brightness=0.2, auto_write=False, pixel_order=neopixel.RGB)

RED = (255, 0, 0)
YELLOW = (255, 180, 0)
OY = (255, 100, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
H_CYAN = (0, 130, 130)
BLUE = (0, 0, 102)
DBLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
WHITE = (255, 255, 255)
OFF = (0, 0, 0)
ORANGE = (255, 60, 0)
RO = (255, 30, 0)
# ORANGE = (255, 85, 0)
GREEN1 = (0, 125, 0)
ORANGE1 = (255, 50, 0)
BULB_WHITE = (255, 150, 45)

colors = [RED, YELLOW, GREEN, DBLUE, WHITE]
xmasColors = [RED, WHITE, GREEN]
peppermintColors = [RED, GREEN]
winterColors = [DBLUE, BLUE, H_CYAN, CYAN, WHITE]
treeColors = winterColors

#CHRISTMAS_DAY = 359
count = 0

def setPixel(y, x, color):
    # convert the x and y to a pixel position
    if y % 2 == 0:
        p = width * (y-1) + (width-x) # 40 + 40 - 1
    else:
        p = width * (y-1) + (x-1) # 40 * (3-1) + (2-1) = 80 + 1 = 81

    # set the pixel color
    #print(p)
    pixels[p] = color

def _setPixel(y, x, color):
    x = 21 - x
    y = 21 - y
    # convert the x and y to a pixel position
    if y % 2 == 0:
        p = width * (y-1) + (width-x) # 40 + 40 - 1
    else:
        p = width * (y-1) + (x-1) # 40 * (3-1) + (2-1) = 80 + 1 = 81

    # set the pixel color
    #print(p)
    pixels2[p] = color

def setPixelsX(xArr, y, color):
    for x in xArr:
        setPixel(x, y, color)

def setPixelsY(x, yArr, color):
    for y in yArr:
        setPixel(x, y, color)

def _setPixelsY(x, yArr, color):
    for y in yArr:
        _setPixel(x, y, color)

def drawDaysToGo(dx, dy, color):
    #1-3 6-9 11 13 15-18,1
    setPixelsX(map(lambda x:x+dx, [1,2,3,6,7,8,9,11,13,15,16,17,18]), 1+dy, color)
    #1 4 6 9 11 13 15,2
    setPixelsX(map(lambda x:x+dx, [1,4,6,9,11,13,15]), 2+dy, color)
    #1 4 6-9 11-13 15-18, 3
    setPixelsX(map(lambda x:x+dx, [1,4,6,7,8,9,11,12,13,15,16,17,18]), 3+dy, color)
    #1 4 5 9 12 18,4
    setPixelsX(map(lambda x:x+dx, [1,4,6,9,12,18]), 4+dy, color)
    #1-3 6-9 12 15-18,5
    setPixelsX(map(lambda x:x+dx, [1,2,3,6,9,12,15,16,17,18]), 5+dy, color)
    #4-8 10-13, 8
    setPixelsX(map(lambda x:x+dx, [4,5,6,7,8,10,11,12,13]), 8+dy, color)
    #6 10 13, 9
    setPixelsX(map(lambda x:x+dx, [6,10,13]), 9+dy, color)
    #6 10 13, 10
    setPixelsX(map(lambda x:x+dx, [6,10,13]), 10+dy, color)
    #6 10 13, 11
    setPixelsX(map(lambda x:x+dx, [6,10,13]), 11+dy, color)
    #6 10-13, 12
    setPixelsX(map(lambda x:x+dx, [6,10,11,12,13]), 12+dy, color)
    #5-8 10-13, 14
    setPixelsX(map(lambda x:x+dx, [5,6,7,8,10,11,12,13]), 14+dy, color)
    #5 10 13, 15
    setPixelsX(map(lambda x:x+dx, [5,10,13]), 15+dy, color)
    #5 7 8 10 13, 16
    setPixelsX(map(lambda x:x+dx, [5,7,8,10,13]), 16+dy, color)
    #5 10 13, 17
    setPixelsX(map(lambda x:x+dx, [5,8,10,13]), 17+dy, color)
    #5-8 10-13, 18
    setPixelsX(map(lambda x:x+dx, [5,6,7,8,10,11,12,13]), 18+dy, color)

def drawToGo(dx, dy, color):
    #4-8 10-13, 8
    setPixelsX(map(lambda x:x+dx, [4,5,6,7,8,10,11,12,13]), 8+dy, color)
    #6 10 13, 9
    setPixelsX(map(lambda x:x+dx, [6,10,13]), 9+dy, color)
    #6 10 13, 10
    setPixelsX(map(lambda x:x+dx, [6,10,13]), 10+dy, color)
    #6 10 13, 11
    setPixelsX(map(lambda x:x+dx, [6,10,13]), 11+dy, color)
    #6 10-13, 12
    setPixelsX(map(lambda x:x+dx, [6,10,11,12,13]), 12+dy, color)
    #5-8 10-13, 14
    setPixelsX(map(lambda x:x+dx, [5,6,7,8,10,11,12,13]), 14+dy, color)
    #5 10 13, 15
    setPixelsX(map(lambda x:x+dx, [5,10,13]), 15+dy, color)
    #5 7 8 10 13, 16
    setPixelsX(map(lambda x:x+dx, [5,7,8,10,13]), 16+dy, color)
    #5 10 13, 17
    setPixelsX(map(lambda x:x+dx, [5,8,10,13]), 17+dy, color)
    #5-8 10-13, 18
    setPixelsX(map(lambda x:x+dx, [5,6,7,8,10,11,12,13]), 18+dy, color)


def drawZero(dx, dy, color):
    #1-9, 1 2 19 20
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 19+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 20+dy, color)
    #1, 1-20
    setPixelsY(1+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    #2, 1-20
    setPixelsY(2+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    #8, 1-20
    setPixelsY(8+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    #9, 1-20
    setPixelsY(9+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)

def drawOne(dx, dy, color):
    #5, 1-20
    #6, 1-20
    setPixelsY(5+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(6+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)

def drawTwo(dx, dy, color):
    #1-9 , 1 2 10 11 19 20
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 11+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 19+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 20+dy, color)
    #1, 12-18
    #2, 12-18
    setPixelsY(1+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18,19]), color)
    setPixelsY(2+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18,19]), color)
    #8, 3-9
    #9, 3-9
    setPixelsY(8+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)

def drawThree(dx, dy, color):
    #1-9 , 1
    #1-9 , 2
    #3-9, 10
    #3-9, 11
    #1-9, 19
    #1-9, 20
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [3,4,5,6,7,8,9]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [3,4,5,6,7,8,9]), 11+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 19+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 20+dy, color)
    #8, 1-20
    #9, 1-20
    setPixelsY(8+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    #1, 12-18
    #2, 12-18
#    setPixelsY(1+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18]), color)
#    setPixelsY(2+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18]), color)
    #8, 3-9
    #9, 3-9
    setPixelsY(8+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)

def drawFour(dx, dy, color):
    # 3-7, 10 11
    setPixelsX(map(lambda x:x+dx, [3,4,5,6,7]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [3,4,5,6,7]), 11+dy, color)
    #1 2, 1-11
    setPixelsY(1+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11]), color)
    setPixelsY(2+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11]), color)
    #8, 1-20
    #9, 1-20
    setPixelsY(8+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)

def drawFive(dx, dy, color):
    #1-9, 1 2 10 11 19 20
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 11+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 19+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 20+dy, color)
    #1 2, 3-9
    setPixelsY(1+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)
    setPixelsY(2+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)
    #8 9, 12-18
    setPixelsY(8+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18]), color)

def drawSix(dx, dy, color):
    #1-9, 1 2 10 11 19 20
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 11+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 19+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 20+dy, color)
    #1 2, 3-18
    setPixelsY(1+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]), color)
    setPixelsY(2+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]), color)
    #8 9, 12-18
    setPixelsY(8+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [12,13,14,15,16,17,18]), color)

def drawSeven(dx, dy, color):
    #1-9, 1 2
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    #1 2, 3
    setPixelsX(map(lambda x:x+dx, [1,2]), 3+dy, color)
    #8 9, 3-20
    setPixelsY(8+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)

def drawEight(dx, dy, color):
    #1-9, 1 2 10 11 19 20
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 11+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 19+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 20+dy, color)
    #1 2 8 9, 1-20
    setPixelsY(1+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(2+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(8+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)

def drawNine(dx, dy, color):
    #1-9, 1 2 10 11
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 1+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 2+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 10+dy, color)
    setPixelsX(map(lambda x:x+dx, [1,2,3,4,5,6,7,8,9]), 11+dy, color)
    #1 2, 3-9
    setPixelsY(1+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)
    setPixelsY(2+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9]), color)
    #8 9, 3-20
    setPixelsY(8+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)
    setPixelsY(9+dx,map(lambda y:y+dy, [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]), color)

def drawDigit(num, dx, dy, color):
    if num == 0:
        drawZero(dx, dy, color)
    elif num == 1:
        drawOne(dx, dy, color)
    elif num == 2:
        drawTwo(dx, dy, color)
    elif num == 3:
        drawThree(dx, dy, color)
    elif num == 4:
        drawFour(dx, dy, color)
    elif num == 5:
        drawFive(dx, dy, color)
    elif num == 6:
        drawSix(dx, dy, color)
    elif num == 7:
        drawSeven(dx, dy, color)
    elif num == 8:
        drawEight(dx, dy, color)
    elif num == 9:
        drawNine(dx, dy, color)

def drawMemorial(dx, dy):
    _setPixelsY(1, [1,2,3,4,5], DBLUE)
    _setPixelsY(2, [1,2,3,4,5], DBLUE)
    _setPixelsY(3, [4,5], DBLUE)
    _setPixelsY(4, [4,5], DBLUE)
    _setPixelsY(5, [4,5], DBLUE)
    _setPixelsY(6, [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20], DBLUE)
    _setPixelsY(7, [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,19,20], DBLUE)
    _setPixelsY(10, [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,19,20], DBLUE)
    _setPixelsY(11, [1,2,3,4,5,6,7,8,9,11,12,13,14,15,16,19,20], DBLUE)
    _setPixelsY(12, [11,12,15,16,19,20], DBLUE)
    _setPixelsY(13, [11,12,15,16,19,20], DBLUE)
    _setPixelsY(14, [11,12,15,16,17,18,19,20], DBLUE)
    _setPixelsY(15, [11,12,15,16,17,18,19,20], DBLUE)
    _setPixelsY(17, [1,2,3,4,5,6,7,8,9], DBLUE)
    _setPixelsY(18, [1,2,3,4,5,6,7,8,9], DBLUE)

digitOne = 0
digitTwo = 0
sleepTime = 600
sleepTime = 0.75
threshold = 10
digitColor = RED
textColor = GREEN
colors=[RED, RO, ORANGE, OY, YELLOW, OY, ORANGE, RO]
arms1 = 0
blink1 = 0
arms2 = 0
blink2 = 0

while True:
    if (count == 0 ):
        pixels.fill( OFF )
        pixels.show()
        # get the time until christmas 12/25 is day 359 (http://worldtimeapi.org/api/timezone/America/New_York)
        # so, 359 - this day number = days until Christmas
        if daysToGo < threshold and daysToGo != 0:
            sleepTime = 0.75
        # get 100s place
        digitOne = int(daysToGo/100)
        # get 10s place
        digitTwo = int(daysToGo/10)
        if digitTwo > 9:
            digitTwo = digitTwo % 10
        # get 1s place
        digitThree = daysToGo % 10
        print('Days until Christmas: ', daysToGo)
        print('Hundreds digit: ', digitOne)
        print('Tens digit: ', digitTwo)
        print('Ones digit: ', digitThree)
        # get day of hanukkah
        chanDay = curDay - 352 + 1 if curDay < 359 else 8
        print('Hanukkah: ', chanDay)

    if daysToGo < 100:
        if count % 2 == 0 and daysToGo < threshold:
            pixels.fill(OFF)
        else:
            # draw 10s place;
            drawDigit(digitTwo, 0, 0, digitColor)
            # draw 1s place
            drawDigit(digitThree, 11, 0, digitColor)
        # draw text
        drawDaysToGo(22,0,textColor)
    else:
        # draw 100s place;
        drawDigit(digitOne, 0, 0, digitColor)
        # draw 10s place;
        drawDigit(digitTwo, 11, 0, digitColor)
        # draw 1s place
        drawDigit(digitThree, 22, 0, digitColor)
        drawToGo(27, -3, textColor)
    pixels.show()
    # draw menorah with correct number of candles
    showFile(pixels2, f'json/day_{chanDay}.json')
    pixels2[0] = OFF
    #drawMemorial(0,0)
    pixels2.show()

    if count == 0:
        print(f"Cycle - {count} done. Error: ({errorFlag})")
    count += 1
    time.sleep(sleepTime)
