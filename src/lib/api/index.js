const express = require('express');
const bodyParser = require('body-parser');
const { port } = require('../config');
const { Server } = require('ws');
const { createServer } = require('http');
const { dispatch } = require('../store');
const { audioLevel } = require('../store/actions/channels');

const store = require('./store');
const recording = require('./recording');

const app = express();
const server = createServer(app);

const wss = new Server({
    server
});

wss.on('connection', (ws, req) => {
    ws.on('message', msg => {
        try {
            const payload = JSON.parse(msg);
            dispatch(audioLevel(payload));
        }catch (err) {
            console.error(err);
        }
    });
});

app.use(bodyParser.json());
app.use('/store', store);
app.use('/recording', recording);

server.listen(port);
