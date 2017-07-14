const { CHANNEL_AUDIO_LEVEL } = require('../actions/channels');
const { OPEN_SESSION_SUCCESS } = require('../actions/session');

const initialState = {
    1: {
        level: 0,
        name: 'MAIN L'
    },
    2: {
        level: 0,
        name: 'MAIN R'
    },
    3: {
        level: 0,
        name: 'AUX 1'
    },
    4: {
        level: 0,
        name: 'AUX 2'
    },
    5: {
        level: 0,
        name: 'AUX 3'
    },
    6: {
        level: 0,
        name: 'AUX 4'
    }
};

module.exports = (state = initialState, action) => {
    switch (action.type) {
        case OPEN_SESSION_SUCCESS:
            return state; // @TODO: read names
        case CHANNEL_AUDIO_LEVEL:
            return Object.assign({}, state, {
                [action.payload.channel]: {
                    name: state[action.payload.channel].name,
                    level: action.payload.level
                }
            });
        default:
            return state;
    }
};
