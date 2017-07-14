const CHANNEL_AUDIO_LEVEL = '[Channel] Audio Level';

const audioLevel = level => ({
    type: CHANNEL_AUDIO_LEVEL,
    payload: level
});

module.exports = {
    CHANNEL_AUDIO_LEVEL,
    audioLevel
};
