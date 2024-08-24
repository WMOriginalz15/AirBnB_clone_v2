#!/usr/bin/python3
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def greet_hbnb():
    """Respond with a simple 'Hello HBNB!' message."""
    return "Hello HBNB!"

@app.route('/hbnb')
def show_hbnb():
    """Respond with 'HBNB'."""
    return "HBNB"

@app.route('/c/<text>')
def show_c_text(text):
    """Display 'C' followed by the provided text, replacing underscores with spaces."""
    text = text.replace('_', ' ')
    return f"C {text}"

@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def show_python_text(text):
    """Display 'Python' followed by the provided text, with underscores replaced by spaces."""
    text = text.replace('_', ' ')
    return f"Python {text}"

@app.route('/number/<int:n>')
def show_number(n):
    """Confirm that the given value is an integer by displaying it."""
    return f"{n} is a number"

@app.route('/number_template/<int:n>')
def show_number_template(n):
    """Render an HTML page displaying the provided number inside an H1 tag."""
    return render_template('number.html', n=n)

if __name__ == '__main__':
    # Run the Flask application on 0.0.0.0, port 5000
    app.run(host='0.0.0.0', port=5000)
