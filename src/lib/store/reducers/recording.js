const { START_RECORDING, STOP_RECORDING } = require('../actions/recording');
const { OPEN_SESSION_SUCCESS } = require('../actions/session');

const initialState = {
    active: false,
    files: [],
    channels: [
        [1, 2]
    ]
}

module.exports = (state = initialState, action) => {
    switch (action.type) {
        case OPEN_SESSION_SUCCESS:
            return {
                active: false,
                files: [],
                channels: action.payload.channels
            };
        case START_RECORDING:
            return Object.assign({}, state, {
                active: true,
                files: state.channels.map((channels, i) => {
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
        default:
            return state;
    }
};
