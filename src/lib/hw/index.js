const { gpio, threshold } = require('../config');
let api;

try {
    api = require('./native');
}catch (err) {
    console.warn('Wiring Pi could not be loaded, defaulting to stubs');
    api = require('./stubs');
}

const level = (channel, level) => {
    const config = gpio.leds.channels.find(led => led.channel === channel);
    if (config) {
        for (let i = 0; i < 4; i++) {
            api.digitalWrite(config.base + i, level > threshold[i] ? 1 : 0);
        }
    }
};

const blink = (port, interval = 500) => {
    let value = 1;
    let timeout = setInterval(() => {
        api.digitalWrite(port, value);
        value = value ? 0 : 1;
    }, interval);
    return () => clearInterval(timeout);
};

module.exports = Object.assign({}, api, {
    level,
    blink
});
