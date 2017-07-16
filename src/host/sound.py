import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GObject, Gtk, GstAudio
from .store import store, actions

GObject.threads_init()
Gst.init(None)

base = '/Users/max/Documents/Code/recording-pi/'

recorders = []

def setup_recorder(channels):
    print 'setup start'
    bin = Gst.Bin()
    queue = Gst.ElementFactory.make('queue', 'Queue')
    deinterleave = Gst.ElementFactory.make('deinterleave', None)
    bin.add(queue)
    bin.add(deinterleave)
    queue.link(deinterleave)
    for channel in channels:
        recorder = create_recorder_bin(base + channel['filename'], len(channel['channels']))
        recorders.append({
            'element': recorder,
            'channels': channel['channels']
        })
        bin.add(recorder)

    def on_pad_added(element, pad):
        name = pad.get_name()
        print 'on_pad_added', name
        for recorder in recorders:
            for id, channel in enumerate(recorder['channels']):
                if name == 'src_%(channel)d' % {'channel': channel - 1}:
                    print 'linking pads'
                    sink = recorder['element'].get_static_pad('sink_%(channel)d' % {'channel': id})
                    pad.link(sink)


    deinterleave.connect('pad-added', on_pad_added)

    sink = queue.get_static_pad('sink')
    ghostsink = Gst.GhostPad.new('sink', sink)
    bin.add_pad(ghostsink)
    print 'setup end'
    return bin

def attach_recorder(recorder):
    print 'attach start'
    pipeline.add(recorder)
    tee.link(recorder)
    recorder.set_state(Gst.State.PLAYING)
    print 'attach end'

def detach_recorder(recorder):
    print 'detach start'
    recorder.set_state(Gst.State.NULL)
    pipeline.remove(recorder)
    print 'detach end'

def create_level_bin():
    bin = Gst.Bin()
    queue = Gst.ElementFactory.make('queue', 'Queue')
    level = Gst.ElementFactory.make('level', 'Level')
    fakesink = Gst.ElementFactory.make('fakesink', 'Fake Consumer')
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

def create_recorder_bin(path, sinks=1):
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
            levels = []
            for idx, value in enumerate(array_val):
                level = pow(10, value / 20)
                levels.append({
                    'level': level,
                    'channel': idx + 1
                })
            store.dispatch(actions.audioLevel(levels))

def close():
    pipeline.set_state(Gst.State.NULL)

def start():
    pipeline.set_state(Gst.State.PLAYING)

pipeline = Gst.Pipeline()
src = Gst.ElementFactory.make('autoaudiosrc', 'src')
convert = Gst.ElementFactory.make('audioconvert', None)
tee = Gst.ElementFactory.make('tee', None)

level = create_level_bin()

pipeline.add(src)
pipeline.add(convert)
pipeline.add(tee)
pipeline.add(level)

src.link(convert)
convert.link(tee)
tee.link(level)

bus = pipeline.get_bus()
bus.add_signal_watch()
bus.connect("message", on_message)
