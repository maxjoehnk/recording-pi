const { digitalWrite, wiringPiSetup, mcp23008Setup, pinMode, INPUT, OUTPUT } = require('wiring-pi');
const { gpio } = require('../config');

const setup = () => {
    wiringPiSetup();
    gpio.mcps.forEach(mcp =>
        mcp23008Setup(mcp.offset, mcp.address));
    pinMode(gpio.recordBtn, INPUT);
    pinMode(gpio.leds.recording, OUTPUT);
    gpio.leds.channels.forEach(channel => {
        pinMode(channel.base + 0, OUTPUT);
        pinMode(channel.base + 1, OUTPUT);
        pinMode(channel.base + 2, OUTPUT);
        pinMode(channel.base + 3, OUTPUT);
    });
    gpio.leds.links.forEach(link =>
        pinMode(link.port, OUTPUT));
};

module.exports = {
    digitalWrite,
    setup
};
