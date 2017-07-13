from host.gtk import *
from host.sound import *
from host.api import api
from gevent import Greenlet, spawn, sleep, joinall
import signal
import sys

gtk = GTKMainLoopThread()
gtk.start()

server = api.setup()
serverThread = spawn(server.serve_forever)

def shutdown(signum, frame):
    print 'shutting down'
    detach_recorder()
    close()
    gtk.running = False;
    sys.exit()

signal.signal(signal.SIGINT, shutdown);

start()

joinall([gtk, serverThread])
