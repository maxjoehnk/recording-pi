recording = False

def start(channels):
    recording = True
    print 'Start'
    print channels

def stop():
    recording = False
    print 'Stop'

def isRecording():
    return recording
