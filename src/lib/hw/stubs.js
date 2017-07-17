const { gpio } = require('../config');
const d = require('debug')('recording-pi:hardware:stub');

const setup = () => {
    d('Setting up');
};

const digitalWrite = (port, value) => {
    d(`Setting ${port} to ${value}`);
};

module.exports = {
    digitalWrite,
    setup
};
