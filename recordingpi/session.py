from datetime import datetime

class Session:
    def __init__(self, date=datetime.now()):
        self.date = date;
