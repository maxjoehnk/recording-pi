const express = require('express');
const bodyParser = require('body-parser');
const { port } = require('../config');

const store = require('./store');
const recording = require('./recording');

const app = express();

app.use(bodyParser.json());
app.use('/store', store);
app.use('/recording', recording);

app.listen(port);
