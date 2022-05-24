#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def task_0():
    """returns Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def task_1():
    """returns HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def task_2(text):
    """returns HBNB"""
    msm = text.replace('_', ' ')
    return ("C %s" % msm)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
