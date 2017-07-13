from flask import Flask
from gevent.wsgi import WSGIServer
from .recording import router as recording

app = Flask(__name__)
app.register_blueprint(recording, url_prefix='/recording')

def setup():
    http_server = WSGIServer(('', 5000), app)
    return http_server
