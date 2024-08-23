#!/usr/bin/python3
"""
Flask web application setup
"""

from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route('/', strict_slashes=False)
def home():
    """Handles requests to the root URL and returns a welcome message."""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """Handles requests to the /hbnb URL and returns 'HBNB'."""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    """Displays “C ” followed by the provided text, with underscores replaced by spaces."""
    return 'C ' + text.replace('_', ' ')

if __name__ == '__main__':
    # Run the Flask application on all available IP addresses at port 5000
    app.run(host='0.0.0.0', port=5000)
