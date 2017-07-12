const { call, put, takeEvery, select } = require('redux-saga/effects');
const { OPEN_SESSION, openSessionSuccess, openSessionFailed, SAVE_SESSION, saveSessionSuccess, saveSessionFailed } = require('../actions/session');
const Session = require('../../session');
const { getSession, getPath } = require('../selectors/session');

function* open(action) {
    try {
        const session = yield Session.open(action.payload);
        yield put(openSessionSuccess(session));
    }catch (error) {
        yield put(openSessionFailed(error));
    }
}

function* save(action) {
    try {
        const session = yield select(getSession);
        const file = yield select(getPath);
        yield Session.save(session, file);
        yield put(saveSessionSuccess());
    }catch (error) {
        yield put(saveSessionFailed(error));
    }
}

function* sessionSaga() {
    yield takeEvery(OPEN_SESSION, open);
    yield takeEvery(SAVE_SESSION, save);
}

module.exports = sessionSaga;
