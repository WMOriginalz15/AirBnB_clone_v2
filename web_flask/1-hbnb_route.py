#!/usr/bin/python3
"""
Flask web application initialization
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def home():
    """Handles requests to the root URL and returns a welcome message."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """Handles requests to /hbnb URL and returns 'HBNB'."""
    return 'HBNB'


if __name__ == '__main__':
    # Start the Flask application, making it accessible on all IP addresses 
    # at port 5000
    app.run(host='0.0.0.0', port=5000)
