from gevent import monkey

monkey.patch_all()

import os
from flask_cors import CORS
from flask import Flask, send_from_directory, request, render_template
from flask_socketio import SocketIO

STATIC_FOLDER = 'dist'

app = Flask(__name__, static_folder=STATIC_FOLDER)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
socketio = SocketIO(app)
# store.socketio = socketio



# @app.route('/sounds/alert.mp3')
# def alert_mp3():
#     return send_from_directory('sounds', 'alert.mp3')

# test socket
@app.route('/test')
def test_socket():
    socketio.emit(
        'data',
        {
            'alert_html': "test"
        },
        namespace="/socket/test"
    )
    print "sending"
    return "Done"


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    if(path == ""):
        return send_from_directory(STATIC_FOLDER, 'index.html')
    else:
        if(os.path.exists(STATIC_FOLDER + "/" + path)):
            return send_from_directory(STATIC_FOLDER, path)
        else:
            return send_from_directory(STATIC_FOLDER, 'index.html')


if __name__ == '__main__':
    socketio.run(app, "0.0.0.0", port=5001, threaded=True, debug=True)
