import os
from flask import Flask, send_from_directory, render_template, redirect, url_for, request
from flask_socketio import SocketIO
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS  # comment this on deployment
from src.user import User

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
        print(request.form)
        values = (
            None,
            request.form['First name'],
            request.form['Last name'],
            User.hash_password(request.form['Password']),
            request.form['Age'],
            request.form['Gender'],
            request.form['Email'],
            request.form['Address']
        )
        
        User(*values).create()
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
