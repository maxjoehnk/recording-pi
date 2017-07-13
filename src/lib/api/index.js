const express = require('express');
const bodyParser = require('body-parser');
const { port } = require('../config');

const store = require('./store');

const app = express();

app.use(bodyParser.json());
app.use('/store', store);

app.listen(port);
