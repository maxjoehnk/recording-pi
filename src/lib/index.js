const store = require('./store');
const { newSession } = require('./store/actions/session');

store.dispatch(newSession());
