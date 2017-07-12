from host import display, state
import host.input

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

hasFiles = False;

def render():
    if state == STATE_MENU:
        if currentItem == SELECTED_ITEM_RECORD:
            drawMenu(title, 'Record')
        elif currentItem == SELECTED_ITEM_PLAY:
            drawMenu(title, 'Play', not hasFiles)
        elif currentItem == SELECTED_ITEM_EXPORT:
            drawMenu(title, 'Export', not hasFiles)
        elif currentItem == SELECTED_ITEM_CHANNEL_SETUP:
            drawMenu(title, 'Channel Setup')
        elif currentItem == SELECTED_ITEM_DELETE:
            drawMenu(title, 'Delete', not hasFiles)
        elif currentItem == SELECTED_ITEM_CLOSE:
            drawMenu(title, 'Close')
            if isEncoderBtnPressed():
                return STATE_MAIN_MENU
    dir = getEncoderDirection()
    if dir == 1:
        currentItem += 1
        if currentItem > SELECTED_ITEM_CLOSE:
            currentItem = SELECTED_ITEM_RECORD
    elif dir == -1:
        currentItem -= 1
        if currentItem < SELECTED_ITEM_RECORD:
            currentItem = SELECTED_ITEM_CLOSE
