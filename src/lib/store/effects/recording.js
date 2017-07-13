const { call, put, takeEvery, select } = require('redux-saga/effects');
const { START_RECORDING, STOP_RECORDING } = require('../actions/recording');
const fetch = require('node-fetch');
const { pythonPort } = require('../../config');

function* start(action) {
    try {
        yield fetch(`http://localhost:${pythonPort}/recording/start`, {
            method: 'POST'
        });
    }catch (error) {
        console.error(error);
    }
}

function* stop(action) {
    try {
        yield fetch(`http://localhost:${pythonPort}/recording/stop`, {
            method: 'POST'
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
