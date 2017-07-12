const { call, put, takeEvery, select } = require('redux-saga/effects');
const { OPEN_SESSION, openSessionSuccess, openSessionFailed, SAVE_SESSION, saveSessionSuccess, saveSessionFailed, DELETE_SESSION, deleteSessionSuccess, deleteSessionFailed } = require('../actions/session');
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

function* remove(action) {
    try {
        const session = yield select(getSession);
        const path = yield select(getPath);
        yield Session.remove(session, path);
        yield put(deleteSessionSuccess());
    }catch (error) {
        yield put(deleteSessionFailed(error));
    }
}

function* sessionSaga() {
    yield takeEvery(OPEN_SESSION, open);
    yield takeEvery(SAVE_SESSION, save);
    yield takeEvery(DELETE_SESSION, remove);
}

module.exports = sessionSaga;
