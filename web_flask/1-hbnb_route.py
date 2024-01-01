#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    print helo HBNB
    """
    return 'Hello HBNB!'


@app.route('/', strict_slashes=False)
def hbnb():
    """
    print HBNB
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
