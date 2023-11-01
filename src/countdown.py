import board
import neopixel
import time

from utils.connection import Connection
from utils.matrix import LOWER_LEFT, Matrix
from utils.christmas import ChristmasCounterDowner

# global constants
JSON_URL = "https://d6u9xjk595.execute-api.us-east-1.amazonaws.com/api/day"

# variables that are needed in every cycle of the loop
connection = None
count_downer = None
days_to_go = -1
time_to_change = -1
last_checked = -1
i = 0


def get_days(con: Connection):
    # get the number of days
    json = con.get_json(JSON_URL)
    print(json)
    cur_day = json["day_of_year"]
    days_to_go = json["days_to_christmas"]
    try:
        time_to_change = json["seconds_until_update"]
    except:
        time_to_change = 30000
    print(f'Day of year: {cur_day}')
    print(f'Days till Christmas: {days_to_go}')
    print(f'Time to change: {time_to_change}')
    return days_to_go, time_to_change, time.monotonic_ns()


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
        # create the connection for querying
        connection = Connection(secrets["ssid"], secrets["password"])
        # create the counter downer object
        #matrix = Matrix(width=40, height=20, pin=board.D0, brightness=0.1, auto_write=False, pixel_order=neopixel.RGB, origin=UPPER_LEFT)
        count_downer = ChristmasCounterDowner(
            Matrix(width=40, height=20, pin=board.D10, brightness=0.15, auto_write=False, pixel_order=neopixel.RGB, origin=LOWER_LEFT)
        )
        days_to_go, time_to_change, last_checked = get_days(connection)
        count_downer.set_days(days_to_go)
    else:
        if time.monotonic_ns() - last_checked > time_to_change * 1000000000:
            print('Updating the days to go')
            daysToGo, timeToChange, last_checked = get_days(connection)
            count_downer.set_days(days_to_go)
    i += 1
    time.sleep(1)
