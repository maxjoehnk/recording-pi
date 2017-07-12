const { readFile, writeFile, existsSync, mkdirSync } = require('fs');
const rm = require('rimraf');
const { sessionPath } = require('./config');

const open = (id) => new Promise((resolve, reject) => {
    const path = `${sessionPath}/${id}`;
    readFile(`${path}/session.json`, 'utf8', (err, data) => {
        if (err) {
            return reject(err);
        }
        try {
            return resolve(JSON.parse(data));
        }catch (err) {
            return reject(err);
        }
    });
});

const save = (session, id) => new Promise((resolve, reject) => {
    const path = `${sessionPath}/${id}`;
    if (!existsSync(path)) {
        mkdirSync(path);
    }
    writeFile(`${path}/session.json`, JSON.stringify(session), (err) => {
        if (err) {
            return reject(err);
        }
        return resolve();
    });
});

const remove = (id) => new Promise((resolve, reject) => {
    const path = `${sessionPath}/${id}`;
    rm(path, (err) => {
        if (err) {
            return reject(err);
        }
        return resolve();
    });
});

const empty = () => ({
    name: 'Empty Session',
    date: new Date(),
    channels: [
        [1, 2]
    ],
    recordings: []
});

module.exports = {
    open,
    save,
    empty,
    remove
};
