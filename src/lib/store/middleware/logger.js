const d = require('debug')('recording-pi:store');

module.exports = store => next => action => {
    d(action);
    next(action);
};
