const getSession = state => state.session.current;
const getPath = state => state.session.path;

module.exports = {
    getSession,
    getPath
};
