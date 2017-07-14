import { createStore, compose } from 'redux';
import reducers from './reducers';
import middleware from './middleware';
import { setup as setupSaga } from './middleware/saga';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
    reducers,
    composeEnhancers(
        middleware
    )
);

setupSaga();

export default store;
