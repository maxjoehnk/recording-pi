const { Router } = require('express');
const store = require('../store');

const router = new Router();

router.get('/', (req, res, next) => {
    const state = store.getState();
    res.json(state);
    res.status(200);
    res.end();
});

router.post('/dispatch', (req, res, next) => {
    store.dispatch(req.body);
    res.status(200);
    res.end();
});

module.exports = router;
