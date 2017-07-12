const { createStore } = require('redux');
const { composeWithDevTools } = require('remote-redux-devtools');
const reducers = require('./reducers');
const middleware = require('./middleware');
const { setup: setupSaga } = require('./middleware/saga');

const composeEnhancers = composeWithDevTools({
    port: 8000,
    realtime: true
});

const store = createStore(
    reducers,
    composeEnhancers(
        middleware
    )
);

setupSaga();

module.exports = store;
