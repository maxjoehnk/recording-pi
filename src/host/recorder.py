import sound

recording = False

def start(channels):
    global recorder
    recording = True
    recorder = sound.setup_recorder(channels)
    sound.attach_recorder(recorder)

def stop():
    global recorder
    recording = False
    sound.detach_recorder(recorder)
    recorder = None

def isRecording():
    return recording
