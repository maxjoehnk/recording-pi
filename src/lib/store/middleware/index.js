const { applyMiddleware } = require('redux');
const { middleware: saga } = require('./saga');
const logger = require('./logger');

module.exports = applyMiddleware(saga, logger);
