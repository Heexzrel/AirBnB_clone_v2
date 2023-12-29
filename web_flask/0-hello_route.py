#!/usr/bin/python3
""" Starting a flask web alication
listening on 0.0.0.0, port 5000
Routes: "/" that displays hello world
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """function returns hello world"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
