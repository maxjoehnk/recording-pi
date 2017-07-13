from flask import Blueprint, request
import host.recorder as recorder

router = Blueprint('recording', __name__)

@router.route('/start', methods=['Post'])
def start():
    recorder.start(request.get_json())
    return ('', 204)

@router.route('/stop', methods=['Post'])
def stop():
    recorder.stop()
    return ('', 204)
