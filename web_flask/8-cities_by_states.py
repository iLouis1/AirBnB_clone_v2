#!/usr/bin/python3
"""This starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML page with list of all states and related cities.
"""
from models import storage
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays HTML page with list of all states and related cities.

    States/cities are sorted by name.
    """
    states = storage.all("State")
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Will remove current SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0")
