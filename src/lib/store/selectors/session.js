const getSession = state => state.session.current;
const getId = state => state.session.id;

module.exports = {
    getSession,
    getId
};
