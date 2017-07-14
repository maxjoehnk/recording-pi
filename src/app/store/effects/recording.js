const { call, put, takeEvery, select } = require('redux-saga/effects');
const { START_RECORDING, STOP_RECORDING } = require('../actions/recording');

function* start(action) {
    try {
        yield fetch('/api/recording/start', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }catch (error) {
        console.error(error);
    }
}

function* stop(action) {
    try {
        yield fetch('/api/recording/stop', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
    }catch (error) {
        console.error(error);
    }
}

function* recordingSaga() {
    yield takeEvery(START_RECORDING, start);
    yield takeEvery(STOP_RECORDING, stop);
}

module.exports = recordingSaga;
