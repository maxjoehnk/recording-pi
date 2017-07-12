const { default: createSagaMiddleware } = require('redux-saga');
const sessionSaga = require('../effects/session');

const middleware = createSagaMiddleware();

module.exports = {
    middleware,
    setup: () => {
        middleware.run(sessionSaga);
    }
};
