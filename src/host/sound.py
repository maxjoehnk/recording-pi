import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk

import websocket
import json

ws = websocket.WebSocket()
ws.connect("ws://localhost:3000")  # TODO: move to another file

GObject.threads_init()
Gst.init(None)

def setup_recorder():
    global recordingQueue
    global recordingEncoder
    global recordingOutput
    print 'setup_recorder'
    recordingQueue = Gst.ElementFactory.make('queue', 'Recording Queue')
    recordingEncoder = Gst.ElementFactory.make('wavenc', None)
    recordingOutput = Gst.ElementFactory.make('filesink', None)
    print 'init'
    recordingOutput.set_property('location', '/Users/max/Documents/Code/recording-pi/test.wav')
    print 'set property'
    pipeline.add(recordingQueue)
    pipeline.add(recordingEncoder)
    pipeline.add(recordingOutput)
    print 'pipeline'
    recordingQueue.link(recordingEncoder)
    recordingEncoder.link(recordingOutput)
    print 'link'

def attach_recorder():
    print 'attach'
    tee.link(recordingQueue)
    recordingQueue.set_state(Gst.State.PLAYING)
    recordingEncoder.set_state(Gst.State.PLAYING)
    recordingOutput.set_state(Gst.State.PLAYING)
    print 'attached'

def detach_recorder():
    global recordingQueue
    global recordingEncoder
    global recordingOutput
    print 'detach'
    recordingQueue.set_state(Gst.State.NULL)
    recordingEncoder.set_state(Gst.State.NULL)
    recordingOutput.set_state(Gst.State.NULL)
    pipeline.remove(recordingQueue)
    pipeline.remove(recordingEncoder)
    pipeline.remove(recordingOutput)
    recordingQueue = None
    recordingEncoder = None
    recordingOutput = None
    print 'detached'

def on_message(bus, message):
    t = message.type
    if t == Gst.MessageType.EOS:
        print 'EOS'
    elif t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        print "Error: %s" % err, debug
    elif t == Gst.MessageType.ELEMENT:
        struct = Gst.Message.get_structure(message)
        if struct.get_name() == 'level':
            array_val = struct.get_value('rms')
            for idx, value in enumerate(array_val):
                level = pow(10, value / 20)
                ws.send(json.dumps({ # TODO: move to a callback or something
                    'level': level,
                    'channel': idx + 1
                }))

def close():
    pipeline.set_state(Gst.State.NULL)

def start():
    pipeline.set_state(Gst.State.PLAYING)

pipeline = Gst.Pipeline()
src = Gst.ElementFactory.make('autoaudiosrc', 'src')
tee = Gst.ElementFactory.make('tee', None)

queue = Gst.ElementFactory.make('queue', None)
convert = Gst.ElementFactory.make('audioconvert', None)
level = Gst.ElementFactory.make('level', None)
fakesink = Gst.ElementFactory.make("fakesink", "fakesink")

pipeline.add(src)
pipeline.add(tee)
pipeline.add(queue)
pipeline.add(convert)
pipeline.add(level)
pipeline.add(fakesink)

src.link(tee)
tee.link(queue)
queue.link(convert)
convert.link(level)
level.link(fakesink)

level.set_property('post-messages', True)
fakesink.set_property('sync', True)

bus = pipeline.get_bus()
bus.add_signal_watch()
bus.connect("message", on_message)
