import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_GPIO.MCP230xx as MCP230xx

from .consts import *

def setupGPIO():
    GPIO.setmode(GPIO.BCM)

    # Record Button
    GPIO.setup(RECORD_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(RECORD_LED_PIN, GPIO.OUT)

    # Encoder
    GPIO.setup(ENCODER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENCODER_CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.setup(ENCODER_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    # Setup Channel 1 & 2 LEDs
    global __MCP1
    __MCP1 = MCP230xx.MCP23008(busnum=1, address=MCP_1_ADDRESS)
    __MCP1.setup(0, GPIO.OUT)
    __MCP1.setup(1, GPIO.OUT)
    __MCP1.setup(2, GPIO.OUT)
    __MCP1.setup(3, GPIO.OUT)
    __MCP1.setup(4, GPIO.OUT)
    __MCP1.setup(5, GPIO.OUT)
    __MCP1.setup(6, GPIO.OUT)
    __MCP1.setup(7, GPIO.OUT)

    # Setup Channel 3 & 4 LEDs
    global __MCP2
    __MCP2 = MCP230xx.MCP23008(busnum=1, address=MCP_2_ADDRESS)
    __MCP2.setup(0, GPIO.OUT)
    __MCP2.setup(1, GPIO.OUT)
    __MCP2.setup(2, GPIO.OUT)
    __MCP2.setup(3, GPIO.OUT)
    __MCP2.setup(4, GPIO.OUT)
    __MCP2.setup(5, GPIO.OUT)
    __MCP2.setup(6, GPIO.OUT)
    __MCP2.setup(7, GPIO.OUT)

    # Setup Channel 5 & 6 LEDs
    global __MCP3
    __MCP3 = MCP230xx.MCP23008(busnum=1, address=MCP_3_ADDRESS)
    __MCP3.setup(0, GPIO.OUT)
    __MCP3.setup(1, GPIO.OUT)
    __MCP3.setup(2, GPIO.OUT)
    __MCP3.setup(3, GPIO.OUT)
    __MCP3.setup(4, GPIO.OUT)
    __MCP3.setup(5, GPIO.OUT)
    __MCP3.setup(6, GPIO.OUT)
    __MCP3.setup(7, GPIO.OUT)

def setupDisplay():
    global __DISPLAY
    __DISPLAY = Adafruit_SSD1306.SSD1306_128_32(rst=DISPLAY_RST_PIN, dc=DISPLAY_DC_PIN, spi=SPI.SpiDev(DISPLAY_SPI_PORT, DISPLAY_SPI_DEVICE, max_speed_hz=DISPLAY_SPI_SPEED))

    # Initialize Display
    __DISPLAY.begin()

    __DISPLAY.clear()
    __DISPLAY.display()

def bootAnimation():
    for i in [0, 1, 2, 3]:
        __MCP1.output(3 - i, 1)
        __MCP1.output(i + 4, 1)
        __MCP2.output(3 - i, 1)
        __MCP2.output(i + 4, 1)
        __MCP3.output(3 - i, 1)
        __MCP3.output(i + 4, 1)
        sleep(0.15)

    sleep(1)

    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        __MCP1.output(i, 0);
        __MCP2.output(i, 0);
        __MCP3.output(i, 0);

def closeGPIO():
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        __MCP1.output(i, 0)
        __MCP2.output(i, 0)
        __MCP3.output(i, 0)
    GPIO.cleanup()
