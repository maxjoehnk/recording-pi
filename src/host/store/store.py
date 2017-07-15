import requests

import websocket
import json

ws = websocket.WebSocket()
ws.connect("ws://localhost:4000")

def dispatch(action):
    ws.send(json.dumps(action))
