import gi;
from gi.repository import GObject,Gtk;
from gevent import Greenlet, sleep;
import logging;

logger = logging.getLogger();

class GTKMainLoopThread(Greenlet):
    def __init__(self):
        Greenlet.__init__(self);
        logger.debug("Setting up GTK Main Loop Greenlet")
        self.running = True;

    def _run(self):
        while self.running:
            while Gtk.events_pending():
                Gtk.main_iteration()
            sleep(.1)
