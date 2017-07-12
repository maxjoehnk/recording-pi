const START_RECORDING = '[Recording] Start';
const STOP_RECORDING = '[Recording] Stop';

const startRecording = () => ({
    type: START_RECORDING,
    payload: Date.now()
});

const stopRecording = () => ({
    type: STOP_RECORDING
});

module.exports = {
    START_RECORDING,
    STOP_RECORDING,
    startRecording,
    stopRecording
};
