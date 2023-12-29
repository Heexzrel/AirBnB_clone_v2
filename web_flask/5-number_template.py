#!/usr/bin/python3
"""starting flask web application listening 0.0.0.0:5000
Routes:
/: displays "Hello HBNB!"
/hbnb: dislays "HBNB"
/c/<text>
strict_slashes=False
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """dislays for /"""
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """displays for /hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """defining text for /c/<text>"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text="is cool"):
    """defining text for /python/<text> with default"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>")
def my_number(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def html_temp(n):
    """using templates"""
    return render_template('5-number.html', number=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
