#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask
from markupsafe import escape
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
    return ("C {}".format(escape(text)))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def var_python(text='is cool'):
    """route with text variable"""
    text = text.replace('_', ' ')
    return ("Python {}".format(escape(text)))


@app.route('/number/<int:n>', strict_slashes=False)
def var_num(n):
    """route with num"""
    return ("{} is a number".format(n))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
