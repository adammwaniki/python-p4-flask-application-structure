#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Welcome to my page!</h1>'

@app.route('/<string:username>') # writing it this way ensures that it only takes in strings as the parameter. we can make it a valid int or path or float if we want
def user(username):
    return f'<h1>Profile for {username}</h1>'