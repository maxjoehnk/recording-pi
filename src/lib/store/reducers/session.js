const {
    OPEN_SESSION,
    OPEN_SESSION_SUCCESS,
    OPEN_SESSION_FAILED,
    RENAME_SESSION,
    CLOSE_SESSION,
    NEW_SESSION,
    DELETE_SESSION_SUCCESS
} = require('../actions/session');
const { START_RECORDING } = require('../actions/recording');
const Session = require('../../session');

const initialState = {
    pending: false
};

const reduceSession = (state, action) => {
    switch (action.type) {
        case START_RECORDING:
            return Object.assign({}, state, {
                recordings: [...state.recordings, state.channels.map((channels, i) => `${action.payload}-${i}.wav`)]
            });
        case OPEN_SESSION_SUCCESS:
            return action.payload;
        case RENAME_SESSION:
            return Object.assign({}, state, {
                name: action.payload
            });
        case NEW_SESSION:
            return Session.empty();
        default:
            return state;
    }
};

const reducer = (state = initialState, action) => {
    switch (action.type) {
        case OPEN_SESSION:
            return {
                pending: true,
                id: action.payload
            };
        case OPEN_SESSION_SUCCESS:
            return Object.assign({}, state, {
                pending: false,
                current: reduceSession(state.current, action)
            });
        case OPEN_SESSION_FAILED:
            return Object.assign({}, state, {
                pending: false,
                error: action.error
            });
        case START_RECORDING:
        case RENAME_SESSION:
            return Object.assign({}, state, {
                current: reduceSession(state. current, action)
            });
        case NEW_SESSION:
            return Object.assign({}, state, {
                current: reduceSession(state.current, action),
                id: action.payload
            });
        case DELETE_SESSION_SUCCESS:
        case CLOSE_SESSION:
            return {
                pending: false
            };
        default:
            return state;
    }
};

module.exports = reducer;
