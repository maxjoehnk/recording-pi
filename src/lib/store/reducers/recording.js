const { START_RECORDING, STOP_RECORDING } = require('../actions/recording');
const { OPEN_SESSION_SUCCESS } = require('../actions/session');
const { ARM_CHANNEL, DISARM_CHANNEL, LINK_CHANNELS, UNLINK_CHANNELS } = require('../actions/channels');

const initialState = {
    active: false,
    files: [],
    channels: {
        armed: [
            true,
            false,
            false,
            false,
            false
        ],
        setup: [
            [1, 2],
            [3],
            [4],
            [5],
            [6]
        ]
    }
}

module.exports = (state = initialState, action) => {
    switch (action.type) {
        case OPEN_SESSION_SUCCESS:
            return {
                active: false,
                files: [],
                channels: action.payload.channels // TODO: remap
            };
        case START_RECORDING:
            const channels = state.channels.setup.filter((channels, i) => {
                return state.channels.armed[i];
            });
            return Object.assign({}, state, {
                active: true,
                files: channels.map((channels, i) => {
                    return {
                        filename: `${action.payload}-${i}.wav`,
                        channels: channels
                    };
                })
            });
        case STOP_RECORDING:
            return Object.assign({}, state, {
                active: false,
                files: []
            });
        case ARM_CHANNEL: { // Should we use the index here?
            const armed = state.channels.armed.map((value, i) => {
                if (i === action.payload) {
                    return true;
                }
                return value;
            });
            return Object.assign({}, state, {
                channels: {
                    armed,
                    setup: state.channels.setup
                }
            });
        }
        case DISARM_CHANNEL: { // Should we use the index here?
            const armed = state.channels.armed.map((value, i) => {
                if (i === action.payload) {
                    return false;
                }
                return value;
            });
            return Object.assign({}, state, {
                channels: {
                    armed,
                    setup: state.channels.setup
                }
            });
        }
        case LINK_CHANNELS: { // @TODO: update armed array too
            const setup = [
                ...state.channels.setup.filter((channels) =>
                    !channels.includes(action.payload[0]) && !channels.includes(action.payload[1])),
                action.payload
            ].sort((a, b) => {
                if (a[0] < b[0]) {
                    return -1;
                }else {
                    return 1;
                }
            });
            return Object.assign({}, state, {
                channels: {
                    armed: state.channels.armed,
                    setup: setup
                }
            });
        }
        case UNLINK_CHANNELS: { // @TODO: update armed array too
            const setup = [
                ...state.channels.setup.filter((channels) => JSON.stringify(channels) !== JSON.stringify(action.payload)),
                [action.payload[0]],
                [action.payload[1]]
            ].sort((a, b) => {
                if (a[0] < b[0]) {
                    return -1;
                }else {
                    return 1;
                }
            });
            return Object.assign({}, state, {
                channels: {
                    armed: state.channels.armed,
                    setup: setup
                }
            });
        }
        default:
            return state;
    }
};
