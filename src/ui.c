#include <pigpio.h>

const int RECORD_BUTTON = 26;
const int RECORD_LED = 19;
const int GREEN_1 = 13;
const int GREEN_2 = 6;
const int YELLOW = 5;
const int RED = 0;

int main(int argc, char** argv) {
    if (gpioInitialise() < 0) {
        return 1;
    }

    gpioSetMode(RECORD_BUTTON, PI_INPUT);
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
    
    return gpioTerminate();
}
