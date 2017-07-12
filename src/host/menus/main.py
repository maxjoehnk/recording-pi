from host import display, state
import host.input

SELECTED_ITEM_NEW = 0
SELECTED_ITEM_OPEN = 1
SELECTED_ITEM_SETTINGS = 2

currentItem = SELECTED_ITEM_NEW
title = 'Recording Pi'
hasSessions = False

def render():
    if currentItem == SELECTED_ITEM_NEW:
        drawMenu(title, 'New Session')
        if isEncoderBtnPressed():
            # notify node
            return STATE_SESSION_MENU
    elif currentItem == SELECTED_ITEM_OPEN:
        drawMenu(title, 'Open Session', not hasSessions)
        if isEncoderBtnPressed() and hasSessions:
            return STATE_OPEN_SESSION
    elif currentItem == SELECTED_ITEM_SETTINGS:
        drawMenu(title, 'Settings')
        if isEncoderBtnPressed():
            return STATE_SETTINGS
    dir = getEncoderDirection()
    if dir == 1:
        currentItem += 1
        if currentItem > SELECTED_ITEM_CLOSE:
            currentItem = SELECTED_ITEM_RECORD
    elif dir == -1:
        currentItem -= 1
        if currentItem < SELECTED_ITEM_RECORD:
            currentItem = SELECTED_ITEM_CLOSE
