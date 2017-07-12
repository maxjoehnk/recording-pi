import host.boot
import host.input

from host import state

import host.menus.session
import host.menus.main

from time import sleep

boot.setupGPIO()
boot.setupDisplay()
boot.bootAnimation()

state = STATE_SESSION_MENU

try:
    while True:
        input.capture()
        if state == STATE_SESSION_MENU:
            state = session.render()
        elif state == STATE_MAIN_MENU:
            state = main.render()
        sleep(0.001)
finally:
    boot.closeGPIO()
