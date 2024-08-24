#!/usr/bin/python3
"""
Flask application initialization script
"""

from flask import Flask

# Instantiate the Flask application
app = Flask(__name__)


@app.route('/airbnb-onepage/', strict_slashes=False)
def homepage():
    """Handles the root URL and returns a greeting."""
    return 'Hello HBNB!'


if __name__ == '__main__':
    # Run the application on all available IP addresses
    app.run(host='0.0.0.0', port=5000)
