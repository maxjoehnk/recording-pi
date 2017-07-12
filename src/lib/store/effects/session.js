const { call, put, takeEvery, select } = require('redux-saga/effects');
const { OPEN_SESSION, openSessionSuccess, openSessionFailed, SAVE_SESSION, saveSessionSuccess, saveSessionFailed, DELETE_SESSION, deleteSessionSuccess, deleteSessionFailed } = require('../actions/session');
const Session = require('../../models/session');
const { getSession, getId } = require('../selectors/session');

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
        const id = yield select(getId);
        yield Session.save(session, id);
        yield put(saveSessionSuccess());
    }catch (error) {
        yield put(saveSessionFailed(error));
    }
}

function* remove(action) {
    try {
        const id = yield select(getId);
        yield Session.remove(id);
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
