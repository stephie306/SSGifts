import os
from flask import Flask, send_from_directory, render_template, redirect, url_for
from flask_socketio import SocketIO
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS #comment this on deployment

app = Flask(__name__, static_url_path='', static_folder='static')
CORS(app) #comment this on deployment
api = Api(app)
socket = SocketIO(app)

@app.route("/", defaults={'path':''})
def serve(path):
    return send_from_directory(app.static_folder,'/html/index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    return redirect(app.static_folder, '/html/login.html')

if __name__ == '__main__':
    socket.run(app, debug=False)