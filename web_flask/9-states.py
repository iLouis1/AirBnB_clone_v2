#!/usr/bin/python3
"""This starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /states: HTML page with list of all State objects.
    /states/<id>: HTML page displaying given state with <id>.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """This displays HTML page with list of all States.

    States are sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    """Displays HTML page with info about <id>, if it exists."""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Will remove current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
