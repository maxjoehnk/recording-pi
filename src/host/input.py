import RPi.GPIO as GPIO

from host import consts

global ENCODER_DT_STATE
global ENCODER_CLK_STATE
global ENCODER_CLK_LAST_STATE
global ENCODER_BTN_STATE
global ENCODER_BTN_LAST_STATE

global RECORD_BTN_STATE
global RECORD_BTN_LAST_STATE

def capture():
    # Persist old state
    ENCODER_CLK_LAST_STATE = ENCODER_CLK_STATE
    ENCODER_BTN_LAST_STATE = ENCODER_BTN_STATE
    RECORD_BTN_LAST_STATE = RECORD_BTN_STATE

    # Fetch new State
    ENCODER_CLK_STATE = GPIO.input(ENCODER_CLK_PIN)
    ENCODER_DT_STATE = GPIO.input(ENCODER_DT_PIN)
    ENCODER_BTN_STATE = GPIO.input(ENCODER_BTN_STATE)
    RECORD_BTN_STATE = GPIO.input(RECORD_BUTTON_PIN)

def isRecordBtnPressed():
    if RECORD_BTN_STATE != RECORD_BTN_LAST_STATE:
        if RECORD_BTN_STATE == 1:
            return True
    return False

def isEncoderBtnPressed():
    if ENCODER_BTN_STATE != ENCODER_BTN_LAST_STATE:
        if ENCODER_BTN_STATE == 1:
            return True
    return False

def getEncoderDirection():
    if ENCODER_CLK_STATE != ENCODER_CLK_LAST_STATE:
        if ENCODER_DT_STATE != ENCODER_CLK_STATE:
            return 1
        else:
            return -1
    return 0
