from flask import Flask, request
from flask_socketio import SocketIO
from flask_cors import CORS
import time
from database_handler import DatabaseHandler, Order

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)
db = DatabaseHandler()

# socketio.init_app(app, cors_allowed_origins="*", logger=True, engineio_logger=True)

@socketio.on('connect')
def handle_connect(data):
    # Add client to the list on connection
    print(f'Client connected: {request.sid}')

@socketio.on('disconnect')
def handle_disconnect(data):
    print(f'Client disconnected: {request.sid}')


@app.route("/newOrder", methods=["POST"])
def handle_new_order():
    try:
        order = request.get_json(force=True)["order"]
        order = Order(order)
    except:
        return "error", 400

    order["timestamp"] = time.time()
    db.create_order(order)
    return "success", 200

if __name__ == '__main__':
    db.init()
    db.delete_all_data()
    socketio.run(app, host='0.0.0.0', port=8090, debug=True, use_reloader=False)
