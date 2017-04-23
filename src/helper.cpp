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
