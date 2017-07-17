const { takeEvery, select } = require('redux-saga/effects');
const { CHANNELS_AUDIO_LEVEL, LINK_CHANNELS, UNLINK_CHANNELS } = require('../actions/channels');
const hardware = require('../../hw');
const { gpio } = require('../../config');

function* level(action) {
    action.payload.forEach(channel => {
        hardware.level(channel.channel, channel.level);
    });
}

function* link(action) {
    const identifier = action.payload[0] * 10 + action.payload[1];
    const link = gpio.leds.links.find(link => link.channels === identifier);
    if (link) {
        hardware.digitalWrite(link.port, 1);
    }
}

function* unlink(action) {
    const identifier = action.payload[0] * 10 + action.payload[1];
    const link = gpio.leds.links.find(link => link.channels === identifier);
    if (link) {
        hardware.digitalWrite(link.port, 0);
    }
}

function* channelsSaga() {
    yield takeEvery(CHANNELS_AUDIO_LEVEL, level);
    yield takeEvery(LINK_CHANNELS, link);
    yield takeEvery(UNLINK_CHANNELS, unlink);
}

module.exports = channelsSaga;
