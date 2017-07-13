import sound

recording = False

def start(channels):
    recording = True
    sound.setup_recorder()
    sound.attach_recorder()

def stop():
    recording = False
    sound.detach_recorder()

def isRecording():
    return recording
