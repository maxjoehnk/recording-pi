import RPi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_GPIO.MCP230xx as MCP230xx

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from time import sleep, time

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

# Setup MCP23008 #1
mcp1 = MCP230xx.MCP23008(busnum=1, address=MCP_1_ADDRESS)
mcp1.setup(0, GPIO.OUT)
mcp1.setup(1, GPIO.OUT)
mcp1.setup(2, GPIO.OUT)
mcp1.setup(3, GPIO.OUT)
mcp1.setup(4, GPIO.OUT)
mcp1.setup(5, GPIO.OUT)
mcp1.setup(6, GPIO.OUT)
mcp1.setup(7, GPIO.OUT)

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

# Start Up Animation
for i in [0, 1, 2, 3]:
    mcp1.output(3 - i, 1)
    mcp1.output(i + 4, 1)
    sleep(0.15)

sleep(1)

for i in [0, 1, 2, 3, 4, 5, 6, 7]:
    mcp1.output(i, 0);

def createSession():
    session = Session();
    menu.clear();
    menu.label = "Sessions";
    menu.add(MenuItem("Record", session.record))
    menu.add(MenuItem("Play", session.play))
    menu.add(MenuItem("Delete", session.delete))
    menu.add(MenuItem("Close", closeSession))

def loadSession():
    print "loading Sessions";

def closeSession():
    openMainMenu();

def openMainMenu():
    menu.clear();
    menu.label = "Main Menu";
    menu.add(MenuItem("Create Session", createSession));
    menu.add(MenuItem("Load Session", loadSession));
    menu.add(MenuItem("Exit", exit));

def shutdown():
    for i in [0, 1, 2, 3, 4, 5, 6, 7]:
        mcp1.output(i, 0)
    GPIO.cleanup();

index = 0
clkLastState = GPIO.input(ENCODER_CLK_PIN)
encoderBtnLastState = GPIO.input(ENCODER_BUTTON_PIN);

menu = Menu("Main Menu", []);
openMainMenu();

class RecordLed:
    def __init__(self):
        self.timePassed = 0
        self.active = 1

    def run(self, delta):
        self.timePassed += delta
        if self.timePassed > 0.01:
            if self.active == 1:
                self.active = 0
            else:
                self.active = 1
            GPIO.output(RECORD_LED_PIN, self.active)

led = RecordLed()

lastTime = time()

try:
    while True:
            delta = time() - lastTime

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
            led.run(delta)
            lastTime = time()
            sleep(0.001)
finally:
    shutdown()
