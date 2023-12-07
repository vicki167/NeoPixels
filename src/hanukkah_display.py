import board
import neopixel
import time

from utils.connection import Connection
from utils.hanukkah import Menorah
from utils.matrix import Matrix, UPPER_LEFT

# global constants
JSON_URL = "https://d6u9xjk595.execute-api.us-east-1.amazonaws.com/api/day"

# variables that are needed in every cycle of the loop
connection = None
menorah = None
day = -1
time_to_change = -1
last_checked = -1
i = 0


def get_days(con: Connection):
    # get the number of days
    json = con.get_json(JSON_URL)
    print(json)
    cur_day = json["day_of_year"]
    _day = 340 - cur_day
    try:
        _time_to_change = json["seconds_until_update"]
    except:
        _time_to_change = 30000
    print(f'Day of year: {cur_day}')
    print(f'Day of Hanukkah: {_day}')
    print(f'Time to change: {_time_to_change}')
    return _day, _time_to_change, time.monotonic_ns()

#m = Matrix(width=40, height=20, pin=board.D10, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB, origin=LOWER_RIGHT, offset=0)


while True:
    # initial setup
    if i == 0:
        # TODO - no error handling.  add if needed
        # Get wifi details and more from a secrets.py file
        try:
            from secrets import secrets
        except ImportError:
            print("WiFi secrets are kept in secrets.py, please add them there!")
            raise
        # create the counter downer object
        menorah = Menorah(
            Matrix(width=40, height=20, pin=board.D0, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB, origin=UPPER_LEFT, vertical=False, offset=1)
        )
        # create the connection for querying
        connection = Connection(secrets["ssid"], secrets["password"])
        # get the days
        day, time_to_change, last_checked = get_days(connection)
        menorah.set_day(day)
    else:
        if time.monotonic_ns() - last_checked > time_to_change * 1000000000:
            print('Updating the days to go')
            day, timeToChange, last_checked = get_days(connection)
            menorah.set_day(day)
    i += 1
