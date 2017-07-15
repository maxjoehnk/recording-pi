const express = require('express');
const bodyParser = require('body-parser');
const { ports } = require('../config');
const { Server } = require('ws');
const { createServer } = require('http');
const { dispatch } = require('../store');

const app = express();
const server = createServer(app);

const wss = new Server({
    server
});

wss.on('connection', (ws, req) => {
    ws.on('message', msg => {
        try {
            const payload = JSON.parse(msg);
            dispatch(payload);
        }catch (err) {
            console.error(err);
        }
    });
});

app.use(bodyParser.json());

server.listen(ports.hostApi);
