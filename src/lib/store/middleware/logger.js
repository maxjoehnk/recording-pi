module.exports = store => next => action => {
    console.log(action);
    next(action);
};
