from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('notification')
def handle_notification(data):
    emit('new_notification', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host="0.0.0.0",port=8000)
