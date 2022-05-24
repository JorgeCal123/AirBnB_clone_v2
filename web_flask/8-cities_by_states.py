#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template
from models.state import State
from models import storage
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def task_9():
    """display a HTML page"""
    states = list(storage.all(State).values())
    states = sorted(states, key=lambda x: x.name)
    states_city = {}
    for value in states:
        arrc = sorted(value.cities, key=lambda x: x.name)
        states_city[value] = arrc
    return render_template('8-cities_by_states.html', states_city=states_city)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
