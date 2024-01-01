#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    print helo HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    print HBNB
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def var_text(text):
    """
    route with text variable
    """
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
