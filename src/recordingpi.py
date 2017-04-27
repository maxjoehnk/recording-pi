import Rpi.GPIO as GPIO

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
import Adafruit_MCP230xx.MCP23008 as MCP23008

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# Setup GPIO
RECORD_BUTTON_PIN = 5;
RECORD_LED_PIN = 6;

ENCODER_BUTTON_PIN = 17;
ENCODER_1_PIN = 27;
ENCODER_2_PIN = 22;

GPIO.setmode(GPIO.BCM);

GPIO.setup(RECORD_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(RECORD_LED_PIN, GPIO.OUT);

GPIO.setup(ENCODER_BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(ENCODER_1_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);
GPIO.setup(ENCODER_2_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP);

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
draw.rectangle((10, 10, width - 10, height - 10), outline=0, fill=1);

disp.image(image);
disp.display();

except KeyboardInterrupt:
    GPIO.cleanup();
