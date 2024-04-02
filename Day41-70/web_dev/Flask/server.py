from flask import Flask
import random
game = Flask(__name__)

@game.route("/")
def enter():
    return '<h1>Guess a number between 0 and 9'\
            '<br/><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2N5MXFoc2lsb3FoYmIxOHd3MGdrYjN0Mnd4bTJlMGEwbHRqOWFwaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/BQCsG0FBYjeYkmQ5bs/giphy.gif"/>'

@game.route("/<int:num>")
def user_value(num):
    computer_number = random.randint(0, 9)

    print(computer_number)
    if num == computer_number:
        return '<h2 style="color:green;"> Yes! You are correct</h2> <br/><br/><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYTV4MnNvaTh1ZDB3ZXR0aWg1OG04cG8wYjBleGd4bGVwMDhmbDhzdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3oz8xAFtqoOUUrsh7W/giphy.gif"/>'
    elif num > computer_number:
        return '<h3 style="color:blue;"> You are guessing higher. Try again</h3><br/><br/><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNnc2bjR0MXIycnZzdW05bGJjNTk2ZmswMzRxNjV0Y3dzeTUxZWFpciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/2uwZ4xi75JhxZYeyQB/giphy.gif"/>'
    elif num < computer_number:
        return '<h4 style="color:red;"> You are guessing lower. Try again</h3><br/><br/><img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExeHNzb3RsbDkzbXY2dXk0cTkydXJhZWZoY2w4dG1iYzZhNjEzZWVtbSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/5dzsKw2xDpaYoLu6RK/giphy.gif"/>'


if __name__ == "__main__":
    pass
    game.run(debug=True)