from datetime import datetime

class Session:
    def __init__(self, date=datetime.now()):
        self.date = date;

    def record(self):
        print "recording"

    def play(self):
        print "playing"

    def delete(self):
        print "deleting"

    def close(self):
        print "closing"
