from flask import Flask
import random
card = Flask(__name__)
from flask import render_template

@card.route("/")
def new_website():
    # return "<h1>Hello World</h1>"
    return render_template("index.html")

if __name__ == "__main__":
    card.run(debug=True)
