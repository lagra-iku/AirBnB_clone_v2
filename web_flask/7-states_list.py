#!/usr/bin/python3
"""
starts a flask web application
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
import shlex
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


@app.route('/number_template/<int:n>', strict_slashes=False)
def var_numtemp(n):
    """route with num"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def var_evenodd(n):
    """route with num and check if even or odd"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/states_list')
def call_States():
    """ 
    display a html page
    """
    lista = []
    dic = storage.all("State")
    for elem in dic:
        var = dic[elem].name + "/" + dic[elem].id
        lista.append(var)
    lista.sort()
    lista2 = []
    for elem in lista:
        elem = elem.replace('/', ' ')
        elem = shlex.split(elem)
        lista2.append((elem[0], elem[1]))
    return (render_template('7-states_list.html', tupla=lista2))


@app.teardown_appcontext
def close(var=None):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
