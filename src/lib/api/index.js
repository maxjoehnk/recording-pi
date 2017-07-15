const express = require('express');
const bodyParser = require('body-parser');
const { ports } = require('../config');
const { Server } = require('ws');
const { createServer } = require('http');
const { dispatch } = require('../store');

const recording = require('./recording');

const app = express();
const server = createServer(app);

const wss = new Server({
    server
});

wss.on('connection', (ws, req) => {
    ws.on('message', msg => {
    });
});

app.use(bodyParser.json());
app.use('/recording', recording);

server.listen(ports.clientApi);
