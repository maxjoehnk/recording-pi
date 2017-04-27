from PIL import ImageFont

from .consts import *

font = ImageFont.load_default()

class MenuItem:
    def __init__(self, label, callback):
        self.label = label;
        self.callback = callback;

class Menu:
    def __init__(self, label, items=[]):
        self.label = label;
        self.items = items;
        self.index = 0;

    def render(self, draw):
        # Clear Background
        draw.rectangle((0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT), outline=0, fill=0);
        # Write Title
        draw.text((0, 0), self.label, font=font, fill=255);
        # Write Current Menu Item
        if len(self.items) > 0:
            draw.text((0, 16), self.items[self.index].label, font=font, fill=255);
        else:
            draw.text((0, 16), "No Items", font=font, fill=255);

    def select(self):
        value = self.items[self.index].callback();
        if isinstance(value, Menu):
            self.clear();
            self = value
        return value;

    def next(self):
        self.index += 1;
        if (self.index >= len(self.items)):
            self.index = 0; # Go back to first item

    def prev(self):
        self.index -= 1;
        if (self.index < 0):
            self.index = len(self.items) - 1; # Go Back to last item

    def add(self, item):
        self.items.append(item);

    def clear(self):
        self.items = [];
        self.index = 0;

class SessionMenu(Menu):
    def __init__(self, session):
        Menu.__init__(self, "Session");
        self.add(MenuItem("Record", session.record))
        self.add(MenuItem("Play", session.play))
        self.add(MenuItem("Delete", session.delete))
        self.add(MenuItem("Close", session.close))
