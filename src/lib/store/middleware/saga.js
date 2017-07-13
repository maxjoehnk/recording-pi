const { default: createSagaMiddleware } = require('redux-saga');
const sessionSaga = require('../effects/session');
const recordingSaga = require('../effects/recording');

const middleware = createSagaMiddleware();

module.exports = {
    middleware,
    setup: () => {
        middleware.run(sessionSaga);
        middleware.run(recordingSaga);
    }
};
