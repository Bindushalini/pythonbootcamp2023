from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h2>Hello world</h2>"

@app.route("/new")
def trying_new():
    return "<h2>newly</h2>"


if __name__ == "__main__":
    pass
    app.run()

def do_op(function):
    def wrapper():
        print("entering operation")
        function()
        print("exiting operation")
    return wrapper


@do_op
def sum():
    print("adding")

@do_op
def mult():
    print("multipleing")

sum()
mult()