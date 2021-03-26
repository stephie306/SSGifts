import os
from flask import Flask, send_from_directory, render_template, redirect, url_for
from flask_socketio import SocketIO
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app)  # comment this on deployment
api = Api(app)
socket = SocketIO(app)


@app.route("/")
def homepage():
    return redirect('/html/index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return redirect('/html/login.html')


@socket.on("login")
def socket_login_event():
    return redirect('/login')

@app.route('/register', methods=['GET', 'POST'])
def register():
    return redirect('/html/register.html')


if __name__ == '__main__':
    socket.run(app, debug=False)
