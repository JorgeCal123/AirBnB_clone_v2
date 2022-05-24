#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.route('/states_list', strict_slashes=False)
def task_8():
    """display a HTML page"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda x: x.name)
    return render_template('7-states_list.html', list_states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
