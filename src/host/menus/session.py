from host import display

STATE_MENU = 0
SELECTED_ITEM_RECORD = 0
SELECTED_ITEM_PLAY = 1
SELECTED_ITEM_EXPORT = 2
SELECTED_ITEM_CHANNEL_SETUP = 3
SELECTED_ITEM_DELETE = 4
SELECTED_ITEM_CLOSE = 5

state = STATE_MENU
currentItem = SELECTED_ITEM_RECORD
title = 'Default Session'

def render():
    if state == STATE_MENU:
        if currentItem == SELECTED_ITEM_RECORD:
            drawMenu(title, 'Record')
        elif currentItem == SELECTED_ITEM_PLAY:
            drawMenu(title, 'Play')
