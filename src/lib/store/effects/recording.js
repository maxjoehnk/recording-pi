const { call, put, takeEvery, select } = require('redux-saga/effects');
const fetch = require('node-fetch');
const { START_RECORDING, STOP_RECORDING } = require('../actions/recording');
const { getFiles } = require('../selectors/recording');
const { ports, gpio } = require('../../config');
const { blink } = require('../../hw');

let stopBlinking;

function* start(action) {
    try {
        const files = yield select(getFiles);
        yield fetch(`http://localhost:${ports.python}/recording/start`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(files)
        });
        stopBlinking = blink(gpio.leds.recording);
    }catch (error) {
        console.error(error);
    }
}

function* stop(action) {
    try {
        yield fetch(`http://localhost:${ports.python}/recording/stop`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        if (stopBlinking) {
            stopBlinking();
            stopBlinking = null;
        }
    }catch (error) {
        console.error(error);
    }
}

function* recordingSaga() {
    yield takeEvery(START_RECORDING, start);
    yield takeEvery(STOP_RECORDING, stop);
}

module.exports = recordingSaga;
