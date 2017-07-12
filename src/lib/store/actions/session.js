const OPEN_SESSION = '[Session] Open';
const OPEN_SESSION_SUCCESS = '[Session] Open Success';
const OPEN_SESSION_FAILED = '[Session] Open Failed';
const SAVE_SESSION = '[Session] Save';
const SAVE_SESSION_SUCCESS = '[Session] Save Success';
const SAVE_SESSION_FAILED = '[Session] Save Failed';
const RENAME_SESSION = '[Session] Rename';
const CLOSE_SESSION = '[Session] Close';
const NEW_SESSION = '[Session] New';

const openSession = file => ({
    type: OPEN_SESSION,
    payload: file
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
    type: NEW_SESSION
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
    openSession,
    openSessionSuccess,
    openSessionFailed,
    saveSession,
    saveSessionSuccess,
    saveSessionFailed,
    renameSession,
    closeSession,
    newSession
};
