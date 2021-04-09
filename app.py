import os
from flask import Flask, send_from_directory, render_template, redirect, url_for
from flask_socketio import SocketIO
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
import requests

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='static/html/')
CORS(app)  # comment this on deployment
api = Api(app)
socket = SocketIO(app)


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    elif request.method == 'POST':
        user = User()
        user.first_name = request.form('First name')
        user.last_name = request.form('Last name')
        user.age = request.form('Age')
        user.gender = request.form('Gender')
        user.password = User.hash_password(request.form('Password'))
        user.address = request.form('Address')

        user.create()


if __name__ == '__main__':
    socket.run(app, debug=False)
