const { Router } = require('express');
const store = require('../store');
const { startRecording, stopRecording } = require('../store/actions/recording');

const router = new Router();

router.post('/start', (req, res, next) => {
    store.dispatch(startRecording());
    res.status(200);
    res.end();
});

router.post('/stop', (req, res, next) => {
    store.dispatch(stopRecording());
    res.status(200);
    res.end();
});

module.exports = router;
