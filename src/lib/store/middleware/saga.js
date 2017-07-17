const { default: createSagaMiddleware } = require('redux-saga');
const channelsSaga = require('../effects/channels');
const sessionSaga = require('../effects/session');
const recordingSaga = require('../effects/recording');

const middleware = createSagaMiddleware();

module.exports = {
    middleware,
    setup: () => {
        middleware.run(channelsSaga);
        middleware.run(sessionSaga);
        middleware.run(recordingSaga);
    }
};
