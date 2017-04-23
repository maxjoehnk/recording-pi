#include "helper.h"
#include "ports.h"
#include <pigpio.h>

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

void visualize_rms(int channel, double rms) {
    if (channel === 0) {
        gpioWrite(GREEN_1_L, rms > 0);
        gpioWrite(GREEN_2_L, rms > 0.05);
        gpioWrite(YELLOW_L, rms > 0.07);
        gpioWrite(RED_L, rms > 0.1);
    }else {
        gpioWrite(GREEN_1_R, rms > 0);
        gpioWrite(GREEN_2_R, rms > 0.05);
        gpioWrite(YELLOW_R, rms > 0.07);
        gpioWrite(RED_R, rms > 0.1);
    }
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

int setup() {
    if (gpioInitialise() < 0) {
        return 1;
    }
    gpioSetMode(RECORD_BUTTON, PI_INPUT);
    gpioSetPullUpDown(RECORD_BUTTON, PI_PUD_UP);
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

    return 0;
}

void shutdown() {
    gpioTerminate();
}
