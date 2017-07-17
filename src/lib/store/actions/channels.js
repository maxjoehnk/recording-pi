const CHANNELS_AUDIO_LEVEL = '[Channel] Audio Level';
const ARM_CHANNEL = '[Channel] Arm';
const DISARM_CHANNEL = '[Channel] Disarm';
const LINK_CHANNELS = '[Channel] Link';
const UNLINK_CHANNELS = '[Channel] Unlink';

const audioLevel = level => ({
    type: CHANNELS_AUDIO_LEVEL,
    payload: level
});

const armChannel = index => ({
    type: ARM_CHANNEL,
    payload: index
});

const disarmChannel = index => ({
    type: DISARM_CHANNEL,
    payload: index
});

const linkChannels = channels => ({
    type: LINK_CHANNELS,
    payload: channels
});

const unlinkChannels = channels => ({
    type: UNLINK_CHANNELS,
    payload: channels
});

module.exports = {
    CHANNELS_AUDIO_LEVEL,
    ARM_CHANNEL,
    DISARM_CHANNEL,
    LINK_CHANNELS,
    UNLINK_CHANNELS,
    audioLevel,
    armChannel,
    disarmChannel,
    linkChannels,
    unlinkChannels
};
