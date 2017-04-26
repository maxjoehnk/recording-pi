#include <pigpio.h>
#include "display/ssd1306.h"

const int SERIAL_SPEED = 8000000;
const int RST_PIN = 24;
const int DC_PIN = 25;

const int WIDTH = 128;
const int HEIGHT = 32;
const int PAGES = HEIGHT / 8;
const int buffer_size = WIDTH * PAGES;

int handle;

int* buffer;

int display_init() {
    buffer = (int*) malloc(buffer_size);
    if (buffer == NULL) {
        return 1;
    }
    if ((handle = spiOpen(0, SERIAL_SPEED, 0)) < 0) {
        return 1;
    }
    gpioSetMode(RST_PIN, PI_OUTPUT);
    gpioSetMode(DC_PIN, PI_OUTPUT);
    display_setup();
}

void display_close() {
    free(buffer);
    spiClose(handle);
}

void display_setup() {
    display_write_command(SSD1306_DISPLAYOFF);
    display_write_command(SSD1306_SETDISPLAYCLOCKDIV);
    display_write_command(0x80);
    display_write_command(SSD1306_SETMULTIPLEX);
    display_write_command(0x1F);
    display_write_command(SSD1306_SETDISPLAYOFFSET);
    display_write_command(0x0);
    display_write_command(SSD1306_SETSTARTLINE | 0x0);
    display_write_command(SSD1306_CHARGEPUMP);
    display_write_command(0x14);
    display_write_command(SSD1306_MEMORYMODE);
    display_write_command(0x00);
    display_write_command(SSD1306_SEGREMAP | 0x1);
    display_write_command(SSD1306_COMSCANDEC);
    display_write_command(SSD1306_SETCOMPINS);
    display_write_command(0x02);
    display_write_command(SSD1306_SETCONTRAST);
    display_write_command(0x8F);
    display_write_command(SSD1306_SETPRECHARGE);
    display_write_command(0xF1);
    display_write_command(SSD1306_SETVCOMDETECT);
    display_write_command(0x40);
    display_write_command(SSD1306_DISPLAYALLON_RESUME);
    display_write_command(SSD1306_NORMALDISPLAY);
}

int display_write_command(int cmd) {
    gpioWrite(DC_PIN, 0);
    return spiWrite(handle, [cmd], 1); // Write one byte
}

void display_render() {
    display_write_command(SSD1306_COLUMNADDR);
    display_write_command(0); // Column Start Address
    display_write_command(127); // Column End Address
    display_write_command(SSD1306_PAGEADDR);
    display_write_command(0); // Page Start Address
    display_write_command(3); // Page End Address
    gpioWrite(DC_PIN, 1); // data mode
    spiWrite(handle, buffer, buffer_size);
}

void display_contrast(int contrast) {
    if (contrast < 0 || constrast > 255) {
        return;
    }
    display_write_command(SSD1306_SETCONTRAST);
    display_write_command(contrast);
}

int display_reset() {
    gpioWrite(RST_PIN, 1);
    // sleep 1 ms
    gpioWrite(RST_PIN, 0);
    // sleep 10 ms´
    gpioWrite(RST_PIN, 1);
}

void display_clear_buffer() {
    for (int i = 0; i < buffer_size; i++) {
        buffer[i] = 0;
    }
}

int main(int argc, char** argv) {
    if (gpioInitialise() < 0) {
        return 1;
    }
    if (display_init() != 0) {
        return 1;
    }
    display_clear_buffer();
    display_render();

    display_close();
    gpioTerminate();
    return 0;
}
