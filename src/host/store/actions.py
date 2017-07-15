from uuid import uuid4 as uuid

START_RECORDING = '[Recording] Start'
STOP_RECORDING = '[Recording] Stop'

OPEN_SESSION = '[Session] Open'
SAVE_SESSION = '[Session] Save'
RENAME_SESSION = '[Session] Rename'
CLOSE_SESSION = '[Session] Close'
NEW_SESSION = '[Session] New'
DELETE_SESSION = '[Session] Delete'

CHANNELS_AUDIO_LEVEL = '[Channel] Audio Level'

def newSession():
    return {
        'type': NEW_SESSION,
        'payload': str(uuid())
    }

def audioLevel(levels):
    return {
        'type': CHANNELS_AUDIO_LEVEL,
        'payload': levels
    }
