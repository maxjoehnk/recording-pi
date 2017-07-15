const store = require('./store');
const api = require('./api');
const host = require('./host');

const { newSession } = require('./store/actions/session');

store.dispatch(newSession());
