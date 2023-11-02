# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import board
import terminalio
import time
import adafruit_touchscreen
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_text import label, bitmap_label
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi

# from DisplayUtil import *

# Get wifi details and more from a secrets.py file
try:
    from secrets import secrets
except ImportError:
    print("WiFi secrets are kept in secrets.py, please add them there!")
    raise


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

def time_until_end_of_day(dt=None):
    # type: (datetime.datetime) -> datetime.timedelta
    """
    Get timedelta until end of day on the datetime passed, or current time.
    """
    if dt is None:
        dt = datetime.datetime.now()
    tomorrow = dt + datetime.timedelta(days=1)
    return datetime.datetime.combine(tomorrow, datetime.time.min) - dt

def getDays():
    print("Attempting connection to: ", JSON_URL)
    curDay = 359
    daysToGo = 69
    counter = 0
    errorFlag = False
    notFound = True
    while counter < 3 and notFound:
        try:
            r = requests.get(JSON_URL)
            js = r.json()
            print(js)
            curDay = js["day_of_year"]
            daysToGo = js["days_to_christmas"]
            try:
                timeToChange = js["seconds_until_update"]
            except:
                timeToChange = 30000
            lastChecked = time.monotonic_ns()
            notFound = False
        except Exception as e:
            print(f"Error querying the time server {counter}: ", e)
            time.sleep(0.5)
            counter += 1
            if counter == 3:
                errorFlag = True
                break
            continue
    print(f"Current day: {curDay}")
    print(f"Days to go: {daysToGo}")
    print(f"Seconds to change: {timeToChange}")
    return daysToGo, timeToChange

daysToGo, timeToChange = getDays()
lastChecked = time.monotonic_ns()

MEDIUM_FONT = bitmap_font.load_font("fonts/LeagueSpartan-Bold-16.bdf")
BIG_FONT = bitmap_font.load_font("fonts/LibreBodoniv2002-Bold-27.bdf")


TEXT = f"{daysToGo}"
text_area = label.Label(
    MEDIUM_FONT, text=TEXT, color=0xFF0000, background_color=0x000000, scale=14
)
text_area.x = 0
text_area.y = 0
# centered
text_area.anchor_point = (0.5, 0.5)
text_area.anchored_position = (board.DISPLAY.width // 2, board.DISPLAY.height // 2)
board.DISPLAY.show(text_area)

# touch screen
ts = adafruit_touchscreen.Touchscreen(
    board.TOUCH_XL,
    board.TOUCH_XR,
    board.TOUCH_YD,
    board.TOUCH_YU,
    calibration=((5200, 59000), (5800, 57000)),
    size=(board.DISPLAY.width, board.DISPLAY.height),
)
print(f'width={board.DISPLAY.width}')
print(f'height={board.DISPLAY.height}')

colors=[0x00FF00,0x0000FF,0xFF0000]
i = 0
# interval to check for
while True:
    p = ts.touch_point
    if p:
        print(p)
        text_area.color = colors[i]
        i = (i + 1) % len(colors)
        time.sleep(0.5)

#    print(f'time: {time.monotonic_ns()}')
#    print(f'last: {lastChecked}')
#    print(f'diff: {time.monotonic_ns() - lastChecked}')
#    print(f'changet: {timeToChange}')
    if time.monotonic_ns() - lastChecked > timeToChange * 1000000000:
        print('Updating the days to go')
        daysToGo, timeToChange = getDays()
        lastChecked = time.monotonic_ns()
        TEXT = f"{daysToGo}"
        text_area.text = TEXT

