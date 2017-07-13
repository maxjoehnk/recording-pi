const store = require('./store');
const api = require('./api');

const { newSession } = require('./store/actions/session');

store.dispatch(newSession());
