# Write your code here :-)
__author__ = 'john'

import time

import board
import busio
from digitalio import DigitalInOut
import adafruit_requests as requests
import adafruit_esp32spi.adafruit_esp32spi_socket as socket
from adafruit_esp32spi import adafruit_esp32spi


class Connection:

    def __init__(self, ssid: str, password: str):
        try:
            from secrets import secrets
        except ImportError:
            print("WiFi secrets are kept in secrets.py, please add them there!")
            raise
        # initial setup
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
                # esp.connect_AP(secrets["ssid"], secrets["password"])
                esp.connect_AP(ssid, password)
            except Exception as e:
                counter += 1
                time.sleep(1)
                # going to let this run indefinitely now
                print(f"could not connect to AP, retrying {counter}: ", e)
                continue
        print("Connected to", str(esp.ssid, "utf-8"), "\tRSSI:", esp.rssi)
        print("My IP address is", esp.pretty_ip(esp.ip_address))

    def get_json(self, url: str):
        try:
            r = requests.get(url)
            return r.json()
        except Exception as e:
            print(f"Error querying the time server: ", e)
