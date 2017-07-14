const CHANNELS_AUDIO_LEVEL = '[Channel] Audio Level';

const audioLevel = level => ({
    type: CHANNELS_AUDIO_LEVEL,
    payload: level
});

module.exports = {
    CHANNELS_AUDIO_LEVEL,
    audioLevel
};
