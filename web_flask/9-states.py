#!/usr/bin/python3
"""starts flask listening on 0.0.0.0 port 5000
uses storage to fetch data"""
from flask import Flask, render_template
from models import storage
# from models.state import State


app = Flask(__name__)


def state_list():
    """lists states with their cities"""
    my_states = storage.all("State")
    return render_template("9-states.html", states=my_states)


def state_id(id):
    """displays html page based on id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown_appcontext(exc):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
