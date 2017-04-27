import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_GPIO.MCP230xx as MCP230xx

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from time import sleep

# Setup GPIO
RECORD_BUTTON_PIN = 5;
RECORD_LED_PIN = 6;

ENCODER_BUTTON_PIN = 17;
ENCODER_CLK_PIN = 27;
ENCODER_DT_PIN = 22;

GPIO.setmode(GPIO.BCM);

GPIO.setup(RECORD_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(RECORD_LED_PIN, GPIO.OUT);

GPIO.setup(ENCODER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(ENCODER_CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(ENCODER_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);

# Setup Display
DISPLAY_RST_PIN = 24;
DISPLAY_DC_PIN = 23;
DISPLAY_SPI_PORT = 0;
DISPLAY_SPI_DEVICE = 0;

display = Adafruit_SSD1306.SSD1306_128_32(rst=DISPLAY_RST_PIN, dc=DISPLAY_DC_PIN, spi=SPI.SpiDev(DISPLAY_SPI_PORT, DISPLAY_SPI_DEVICE, max_speed_hz=8000000));

# Initialize Display
display.begin();

# Clear Display
display.clear();
display.display();

width = 128;
height = 32;

image = Image.new('1', (width, height));

draw = ImageDraw.Draw(image);

font = ImageFont.load_default()

index = 0
clkLastState = GPIO.input(ENCODER_CLK_PIN)

menu = ["Create Session", "Load Session"]

try:
    while True:
            #Handle Encoder Rotation
            clkState = GPIO.input(ENCODER_CLK_PIN)
            dtState = GPIO.input(ENCODER_DT_PIN)
            if clkState != clkLastState:
                    if dtState != clkState:
                            index += 1
                    else:
                            index -= 1
                    if index >= menu.length:
                        index = 0
                    else if index < 0:
                        index = menu.length - 1
            clkLastState = clkState

            # Update Display
            # Background
            draw.rectangle((0, 0, width, height), outline=0, fill=0);

            draw.text((0, 0), menu[index]);

            display.image(image)
            display.display()
            sleep(0.001)
finally:
        GPIO.cleanup()
