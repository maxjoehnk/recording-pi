const uuid = require('uuid/v4');

const OPEN_SESSION = '[Session] Open';
const OPEN_SESSION_SUCCESS = '[Session] Open Success';
const OPEN_SESSION_FAILED = '[Session] Open Failed';
const SAVE_SESSION = '[Session] Save';
const SAVE_SESSION_SUCCESS = '[Session] Save Success';
const SAVE_SESSION_FAILED = '[Session] Save Failed';
const RENAME_SESSION = '[Session] Rename';
const CLOSE_SESSION = '[Session] Close';
const NEW_SESSION = '[Session] New';
const DELETE_SESSION = '[Session] Delete';
const DELETE_SESSION_SUCCESS = '[Session] Delete Success';
const DELETE_SESSION_FAILED = '[Session] Delete Failed';

const openSession = id => ({
    type: OPEN_SESSION,
    payload: id
});

const openSessionSuccess = session => ({
    type: OPEN_SESSION_SUCCESS,
    payload: session
});

const openSessionFailed = error => ({
    type: OPEN_SESSION_FAILED,
    error
});

const saveSession = () => ({
    type: SAVE_SESSION
});

const saveSessionSuccess = () => ({
    type: SAVE_SESSION_SUCCESS
});

const saveSessionFailed = error => ({
    type: SAVE_SESSION_FAILED,
    error
});

const renameSession = name => ({
    type: RENAME_SESSION,
    payload: name
});

const closeSession = () => ({
    type: CLOSE_SESSION
});

const newSession = () => ({
    type: NEW_SESSION,
    payload: uuid()
});

const deleteSession = () => ({
    type: DELETE_SESSION
});

const deleteSessionSuccess = () => ({
    type: DELETE_SESSION_SUCCESS
});

const deleteSessionFailed = error => ({
    type: DELETE_SESSION_FAILED,
    error
});

module.exports = {
    OPEN_SESSION,
    OPEN_SESSION_SUCCESS,
    OPEN_SESSION_FAILED,
    SAVE_SESSION,
    SAVE_SESSION_SUCCESS,
    SAVE_SESSION_FAILED,
    RENAME_SESSION,
    CLOSE_SESSION,
    NEW_SESSION,
    DELETE_SESSION,
    DELETE_SESSION_SUCCESS,
    DELETE_SESSION_FAILED,
    openSession,
    openSessionSuccess,
    openSessionFailed,
    saveSession,
    saveSessionSuccess,
    saveSessionFailed,
    renameSession,
    closeSession,
    newSession,
    deleteSession,
    deleteSessionSuccess,
    deleteSessionFailed
};
