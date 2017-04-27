import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_GPIO.MCP230xx as MCP230xx

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from time import sleep

from recordingpi.menu import *
from recordingpi.consts import *
from recordingpi.session import *

# Setup GPIO
GPIO.setmode(GPIO.BCM);

GPIO.setup(RECORD_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(RECORD_LED_PIN, GPIO.OUT);

GPIO.setup(ENCODER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(ENCODER_CLK_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(ENCODER_DT_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);

# Setup Display
display = Adafruit_SSD1306.SSD1306_128_32(rst=DISPLAY_RST_PIN, dc=DISPLAY_DC_PIN, spi=SPI.SpiDev(DISPLAY_SPI_PORT, DISPLAY_SPI_DEVICE, max_speed_hz=8000000));

# Initialize Display
display.begin();

# Clear Display
display.clear();
display.display();

image = Image.new('1', (DISPLAY_WIDTH, DISPLAY_HEIGHT));

draw = ImageDraw.Draw(image);

font = ImageFont.load_default()

# icon = Image.open('miau.ppm').rotate(180).convert('1');
# display.image(icon);
# display.display();

index = 0
clkLastState = GPIO.input(ENCODER_CLK_PIN)
encoderBtnLastState = GPIO.input(ENCODER_BUTTON_PIN);

menu = Menu("Main Menu")

def createSession():
    session = Session();
    m = Menu("Session");
    m.add(MenuItem("Record", session.record))
    m.add(MenuItem("Play", session.play))
    m.add(MenuItem("Delete", session.delete))
    m.add(MenuItem("Close", session.close))
    return m;

def loadSession():
    print "loading Sessions";

menu.add(MenuItem("Create Session", createSession));
menu.add(MenuItem("Load Session", loadSession));
menu.add(MenuItem("Exit", exit));

try:
    while True:
            # Read Inputs
            clkState = GPIO.input(ENCODER_CLK_PIN)
            dtState = GPIO.input(ENCODER_DT_PIN)
            encoderBtnState = GPIO.input(ENCODER_BUTTON_PIN);

            # Handle Encoder Rotation
            if clkState != clkLastState:
                if dtState != clkState:
                    menu.next();
                else:
                    menu.prev();
            clkLastState = clkState

            # Handle Encoder Push
            if encoderBtnState != encoderBtnLastState:
                if GPIO.input(ENCODER_BUTTON_PIN) == 0:
                    if menu is not None:
                        menu.select();
            encoderBtnLastState = encoderBtnState

            if menu is not None:
                menu.render(draw);

            display.image(image.rotate(180))
            display.display()
            sleep(0.001)
finally:
    GPIO.cleanup();
