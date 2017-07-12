const { readFile, writeFile } = require('fs');
const rm = require('rimraf');

const open = (path) => new Promise((resolve, reject) => {
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

const save = (session, path) => new Promise((resolve, reject) => {
    writeFile(`${path}/session.json`, JSON.stringify(session), (err) => {
        if (err) {
            return reject(err);
        }
        return resolve();
    });
});

const remove = (session, path) => new Promise((resolve, reject) => {
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
