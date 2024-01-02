#!/usr/bin/python3
"""starts flask listening on 0.0.0.0 port 5000
uses storage to fetch data"""
from flask import Flask, render_template
from models import storage
# from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown_appcontext(Exception):
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    """displaying all states listed by name"""
    my_states = storage.all("State")
    # sort_state = sorted(states, key=lambda state: state: state.name)
    # sort_states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=my_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
