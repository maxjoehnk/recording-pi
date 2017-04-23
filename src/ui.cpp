#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>
#include <iostream>

const int RECORD_BUTTON = 26;
const int RECORD_LED = 16;
const int GREEN_1 = 13;
const int GREEN_2 = 6;
const int YELLOW = 5;
const int RED = 0;

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
    if (gpioInitialise() < 0) {
        return 1;
    }
    gpioSetMode(RECORD_BUTTON, PI_INPUT);
    gpioSetPullUpDown(RECORD_BUTTON, PI_PUD_UP);
    gpioSetAlertFunc(RECORD_BUTTON, _cb);
    gpioSetMode(RECORD_LED, PI_OUTPUT);
    gpioSetMode(GREEN_1, PI_OUTPUT);
    gpioSetMode(GREEN_2, PI_OUTPUT);
    gpioSetMode(YELLOW, PI_OUTPUT);
    gpioSetMode(RED, PI_OUTPUT);
    gpioWrite(RECORD_LED, 1);
    gpioWrite(GREEN_1, 1);
    gpioWrite(GREEN_2, 1);
    gpioWrite(YELLOW, 1);
    gpioWrite(RED, 1);

    blink_record_led();

    gpioTerminate();
    return 0;
}
