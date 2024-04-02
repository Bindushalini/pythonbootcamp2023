from flask import Flask

app = Flask(__name__)

def make_bold(my_function):
    def wrapper():
        old_string = my_function()
        new_string = f"<b>{old_string}</b>"
        return new_string
    return wrapper

@app.route("/")
def hello_world():
    return "<h2>Hello world</h2>"

@app.route("/new")
@make_bold
def trying_new():
    return "<h2>newly</h2>"

@app.route("/login")
def login_function():
    return f"<h2>Login page</h2>"


@app.route("/<username>")
def load(username):
    return f"<h2>Logged in {username}</h2>"

@app.route("/<username>/<int:number>")
def load_userid(username, number):
    return f"<h2>Logged in {username} with ID : {number}</h2>"

if __name__ == "__main__":
    pass
    app.run(debug=True)

# def do_op(function):
#     def wrapper():
#         print("entering operation")
#         function()
#         print("exiting operation")
#     return wrapper
#
#
# @do_op
# def sum():
#     print("adding")
#
# @do_op
# def mult():
#     print("multipleing")
#
# sum()
# mult()