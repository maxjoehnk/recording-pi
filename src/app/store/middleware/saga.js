const { default: createSagaMiddleware } = require('redux-saga');
const recordingSaga = require('../effects/recording');

const middleware = createSagaMiddleware();

module.exports = {
    middleware,
    setup: () => {
        middleware.run(recordingSaga);
    }
};
