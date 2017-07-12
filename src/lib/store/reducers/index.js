const { combineReducers } = require('redux');

const recording = require('./recording');
const session = require('./session');

module.exports = combineReducers({
    recording,
    session
});
