#!/usr/bin/python3
"""starts flask listening on 0.0.0.0 port 5000
uses storage to fetch data"""
from flask import Flask, render_template
from models import storage
# from models.state import State


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_state():
    """lists states with their cities"""
    my_states = storage.all("State")
    return render_template("8-cities_by_states.html", states=my_states)


@app.teardown_appcontext
def teardown_appcontext(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
