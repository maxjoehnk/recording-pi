const { combineReducers } = require('redux');

const channels = require('./channels');
const recording = require('./recording');
const session = require('./session');

module.exports = combineReducers({
    channels,
    recording,
    session
});
