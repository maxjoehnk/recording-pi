from flask import Flask
from .recording import router as recording

app = Flask(__name__)
app.register_blueprint(recording, url_prefix='/recording')

def setup():
    app.run(debug=True)
