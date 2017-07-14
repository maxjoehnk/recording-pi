const { applyMiddleware } = require('redux');
const { middleware: saga } = require('./saga');

module.exports = applyMiddleware(saga);
