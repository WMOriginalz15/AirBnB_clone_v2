#!/usr/bin/python3
"""
Flask web application module.
"""

from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def welcome():
    """Respond with 'Hello HBNB!' at the root URL."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """Respond with 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """Display 'C' followed by user-provided text, with underscores replaced by spaces."""
    formatted_text = text.replace('_', ' ')
    return f'C {formatted_text}'


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python_text(text='is cool'):
    """Display 'Python' followed by user-provided text, or default to 'is cool'."""
    formatted_text = text.replace('_', ' ')
    return f'Python {formatted_text}'


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    """Confirm and display that the provided value is a number."""
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_with_template(n):
    """Render an HTML page showing the provided number if it's an integer."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    # Start the Flask application, listening on all IP addresses and port 5000
    app.run(host='0.0.0.0', port=5000)

