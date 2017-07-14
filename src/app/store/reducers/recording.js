const { START_RECORDING, STOP_RECORDING } = require('../actions/recording');

module.exports = (state = false, action) => {
    switch (action.type) {
        case START_RECORDING:
            return true;
        case STOP_RECORDING:
            return false;
        default:
            return state;
    }
};
