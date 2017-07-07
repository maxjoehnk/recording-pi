from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

from .boot import __DISPLAY

image = Image.new('1', (DISPLAY_WIDTH, DISPLAY_HEIGHT))

draw = ImageDraw.Draw(image)

font = ImageFont.load_default()

def drawMenu(title, text):
    draw.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=0)
    draw.text((0, 0), title, font=font, fill=255)
    draw.text((0, 16), text, font=font, fill=255)
    __DISPLAY.image(image)
    __DISPLAY.display()
