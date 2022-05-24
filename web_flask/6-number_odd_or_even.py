#!/usr/bin/python3
"""
starts a Flask web application
"""

from flask import Flask, render_template
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
    """returns params text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def task_3(text='is cool'):
    """return default value is cool else params text"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def task_4(n):
    """return param how a number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def task_5(n):
    """modify values in the page html"""
    return render_template('5-number.html', value_number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def task_6(n):
    '''mensagge HBNB'''
    if n % 2 == 0:
        ms = "even"
    else:
        ms = "odd"
    return (render_template("6-number_odd_or_even.html", n=n, ms=ms))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
