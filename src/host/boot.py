import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from .consts import *

def setupGPIO():
    GPIO.setmode(GPIO.BCM)

    # Encoder
    GPIO.setup(ENCODER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENCODER_CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENCODER_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def setupDisplay():
    global __DISPLAY
    __DISPLAY = Adafruit_SSD1306.SSD1306_128_32(rst=DISPLAY_RST_PIN, dc=DISPLAY_DC_PIN, spi=SPI.SpiDev(DISPLAY_SPI_PORT, DISPLAY_SPI_DEVICE, max_speed_hz=DISPLAY_SPI_SPEED))

    # Initialize Display
    __DISPLAY.begin()

    __DISPLAY.clear()
    __DISPLAY.display()

def closeGPIO():
    GPIO.cleanup()
