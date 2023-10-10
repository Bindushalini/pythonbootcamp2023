''' pop up to choose a color : of which tortoise will win the race.
out of rainbow-colored turtle, start the race with random steps.
after the race is complete. Print whether win or loose based on color and print the winner color'''

from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
colors = ["red", "orange", "yellow", "green", "purple", "magenta"]
tim_objects = []
screen.setup(width=500, height=400)
# screen.screensize(500,400)
user_input = screen.textinput("User input", "Select your turtle color?")
if user_input not in colors:
    print("Invalid color selected. ")
    exit()
y_pos = -100
for _ in range(6):
    tim_obj_name = "tim" + str(_)
    tim_obj_name = Turtle("turtle")
    tim_obj_name.color(colors[_])
    tim_obj_name.penup()
    tim_obj_name.setpos(-240, y_pos)
    y_pos += 30
    tim_objects.append(tim_obj_name)

if user_input:
    is_race_on = True
winner = ""
while is_race_on:
    for turt in tim_objects:
        random_number = random.randint(0, 10)
        turt.forward(random_number)
        if turt.xcor() > 230:
            is_race_on = False
            winner = turt.pencolor()
            break
if winner == user_input:
    print(f"You win! The winner color is {user_input}")
else:
    print(f"You loose! The winner color is {winner}")

screen.exitonclick()
