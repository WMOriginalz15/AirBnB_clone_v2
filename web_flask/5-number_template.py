from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Disable strict slashes in route definitions
app.url_map.strict_slashes = False

# Route for the root URL
@app.route('/')
def hello_hbnb():
    return "Hello HBNB!"

# Route for /hbnb
@app.route('/hbnb')
def display_hbnb():
    return "HBNB"

# Route for /c/<text>
@app.route('/c/<text>')
def display_c_text(text):
    formatted_text = text.replace('_', ' ')
    return f"C {formatted_text}"

# Route for /python/(<text>) with a default value
@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def display_python_text(text):
    formatted_text = text.replace('_', ' ')
    return f"Python {formatted_text}"

# Route for /number/<n> that only accepts integers
@app.route('/number/<int:n>')
def display_number(n):
    return f"{n} is a number"

# Route for /number_template/<n> that renders an HTML page
@app.route('/number_template/<int:n>')
def display_number_template(n):
    return render_template('number.html', n=n)

# Start the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

