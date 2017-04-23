#include <stdio.h>
#include <pigpio.h>
#include <unistd.h>
#include <iostream>

const int RECORD_BUTTON = 26;
const int RECORD_LED = 16;
const int GREEN_1_L = 23;
const int GREEN_1_R = 13;
const int GREEN_2_L = 22;
const int GREEN_2_R = 6;
const int YELLOW_L = 27;
const int YELLOW_R = 5;
const int RED_L = 17;
const int RED_R = 0;

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

void set_all(int value) {
    gpioWrite(RECORD_LED, value);
    gpioWrite(GREEN_1_L, value);
    gpioWrite(GREEN_1_R, value);
    gpioWrite(GREEN_2_L, value);
    gpioWrite(GREEN_2_R, value);
    gpioWrite(YELLOW_L, value);
    gpioWrite(YELLOW_R, value);
    gpioWrite(RED_L, value);
    gpioWrite(RED_R, value);
}

void boot() {
    set_all(0);
    gpioWrite(RECORD_LED, 1);
    gpioWrite(GREEN_1_L, 1);
    gpioWrite(GREEN_1_R, 1);
    usleep(100000);
    gpioWrite(GREEN_2_L, 1);
    gpioWrite(GREEN_2_R, 1);
    usleep(100000);
    gpioWrite(YELLOW_L, 1);
    gpioWrite(YELLOW_R, 1);
    usleep(100000);
    gpioWrite(RED_L, 1);
    gpioWrite(RED_R, 1);
    usleep(500000);
    set_all(0);
}

int main(int argc, char** argv) {
    if (gpioInitialise() < 0) {
        return 1;
    }
    gpioSetMode(RECORD_BUTTON, PI_INPUT);
    gpioSetPullUpDown(RECORD_BUTTON, PI_PUD_UP);
    gpioSetAlertFunc(RECORD_BUTTON, _cb);
    gpioSetMode(RECORD_LED, PI_OUTPUT);
    gpioSetMode(GREEN_1_L, PI_OUTPUT);
    gpioSetMode(GREEN_1_R, PI_OUTPUT);
    gpioSetMode(GREEN_2_L, PI_OUTPUT);
    gpioSetMode(GREEN_2_R, PI_OUTPUT);
    gpioSetMode(YELLOW_L, PI_OUTPUT);
    gpioSetMode(YELLOW_R, PI_OUTPUT);
    gpioSetMode(RED_L, PI_OUTPUT);
    gpioSetMode(RED_R, PI_OUTPUT);
    boot();

    blink_record_led();

    gpioTerminate();
    return 0;
}
