import os
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk, GstAudio

GObject.threads_init()
Gst.init(None)

def on_message(bus, message):
    t = message.type
    if t == Gst.MessageType.EOS:
        pass
    elif t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        print "Error: %s" % err, debug
    elif t == Gst.MessageType.ELEMENT:
        struct = Gst.Message.get_structure(message)
        if struct.get_name() == 'level':
            array_val = struct.get_value('rms')
            for idx, value in enumerate(array_val):
                print '%(id)d: %(level)f' % {'id': idx, 'level': pow(10, value / 20)}

def on_pad_added(element, pad):
    sink = None;
    print pad.get_name()
    if pad.get_name() == 'src_0':
        sink = recorder0.get_static_pad('sink_0')
    elif pad.get_name() == 'src_1':
        sink = recorder0.get_static_pad('sink_1')
    elif pad.get_name() == 'src_2':
        pipeline.add(recorder1)
        sink = recorder1.get_static_pad('sink_0')
    elif pad.get_name() == 'src_3':
        pipeline.add(recorder2)
        sink = recorder2.get_static_pad('sink_0')
    else:
        return
    pad.link(sink)

def new_level_bin():
    bin = Gst.Bin()
    queue = Gst.ElementFactory.make('queue', 'Queue')
    level = Gst.ElementFactory.make('level', 'Level')
    fakesink = Gst.ElementFactory.make('fakesink', 'Consumer')
    level.set_property('post-messages', True)
    fakesink.set_property('sync', True)
    bin.add(queue)
    bin.add(level)
    bin.add(fakesink)
    queue.link(level)
    level.link(fakesink)
    sink = queue.get_static_pad('sink')
    ghostpad = Gst.GhostPad.new('sink', sink)
    bin.add_pad(ghostpad)
    return bin

def new_recorder_bin(path, sinks=1):
    bin = Gst.Bin()
    interleave = Gst.ElementFactory.make('interleave', None)
    encoder = Gst.ElementFactory.make('wavenc', None)
    output = Gst.ElementFactory.make('filesink', None)
    output.set_property('location', path)
    bin.add(interleave)
    bin.add(encoder)
    bin.add(output)
    interleave.link(encoder)
    encoder.link(output)
    if sinks == 1:
        queue = Gst.ElementFactory.make('queue', None)
        bin.add(queue)
        interleave.set_property('channel_positions', [GstAudio.AudioChannelPosition.MONO])
        sink = interleave.get_request_pad('sink_0')
        queueSink = queue.get_static_pad('sink')
        queueSrc = queue.get_static_pad('src')
        queueSrc.link(sink)
        ghostpad = Gst.GhostPad.new('sink_0', queueSink)
        bin.add_pad(ghostpad)
    elif sinks == 2:
        queue0 = Gst.ElementFactory.make('queue', 'Queue L')
        queue1 = Gst.ElementFactory.make('queue', 'Queue R')
        bin.add(queue0)
        bin.add(queue1)
        interleave.set_property('channel_positions', [
            GstAudio.AudioChannelPosition.FRONT_LEFT,
            GstAudio.AudioChannelPosition.FRONT_RIGHT
        ])
        sink0 = interleave.get_request_pad('sink_0')
        queueSink0 = queue0.get_static_pad('sink')
        queueSrc0 = queue0.get_static_pad('src')
        queueSrc0.link(sink0)
        ghostpad0 = Gst.GhostPad.new('sink_0', queueSink0)
        sink1 = interleave.get_request_pad('sink_1')
        queueSink1 = queue1.get_static_pad('sink')
        queueSrc1 = queue1.get_static_pad('src')
        queueSrc1.link(sink1)
        ghostpad1 = Gst.GhostPad.new('sink_1', queueSink1)
        bin.add_pad(ghostpad0)
        bin.add_pad(ghostpad1)
    return bin

pipeline = Gst.Pipeline()

src = Gst.ElementFactory.make('autoaudiosrc', 'src')
convert = Gst.ElementFactory.make('audioconvert', 'Convert')
tee = Gst.ElementFactory.make('tee', None)
level = new_level_bin()

recorder = Gst.ElementFactory.make('queue', 'Recording Queue')
deinterleave = Gst.ElementFactory.make('deinterleave', 'Splitter')

recorder0 = new_recorder_bin('/Users/max/Documents/Code/recording-pi/test.wav', 2)
recorder1 = new_recorder_bin('/Users/max/Documents/Code/recording-pi/test-1.wav', 1)
recorder2 = new_recorder_bin('/Users/max/Documents/Code/recording-pi/test-2.wav', 1)

pipeline.add(src)
pipeline.add(convert)
pipeline.add(tee)
pipeline.add(level)
pipeline.add(recorder)
pipeline.add(deinterleave)
pipeline.add(recorder0)

src.link(convert)
convert.link(tee)
tee.link(level)

pipeline.set_state(Gst.State.PLAYING)

bus = pipeline.get_bus()
bus.add_signal_watch()
bus.connect("message", on_message)

deinterleave.connect("pad-added", on_pad_added)

tee.link(recorder)
recorder.link(deinterleave)

Gtk.main()