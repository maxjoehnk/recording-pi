#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>
#include <iostream>
#include "helper.h"
#include "ports.h"

bool recording = false;

static void _cb(int gpio, int level, uint32_t tick) {
    if (level == 1) {
        recording = !recording;
        std::cout << "Recording turned " << (recording ? "on" : "off") << std::endl;
    }
}

void blink_record_led() {
    while (true) {
        gpioWrite(RECORD_LED, recording ? 1 : 0);
        usleep(1000000);
        gpioWrite(RECORD_LED, 0);
        usleep(1000000);
    }
}

int main(int argc, char** argv) {
    setup();
    gpioSetAlertFunc(RECORD_BUTTON, _cb);

    blink_record_led();

    shutdown();
    return 0;
}
