import turtle

import pandas

screen = turtle.Screen()
screen.title("States game")

screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

print(screen.screensize(500,300))

my_states_data = pandas.read_csv("50_states.csv")
name_list = my_states_data.state.to_list()
# print(name_list)
is_guess_on = 0
score = 0
title = "Guess the state"
while is_guess_on < 50:
    answer = screen.textinput(title, "Enter your answer").title()
    if answer == "Exit":
        break
    if answer in name_list:
        matching_row = my_states_data[my_states_data.state == answer]
        x_cord = int(matching_row.x.iloc[0])
        y_cord = int(matching_row.y.iloc[0])
        my_turtle = turtle.Turtle()
        my_turtle.penup()
        my_turtle.hideturtle()
        my_turtle.setposition(x_cord, y_cord)
        my_turtle.write(matching_row.state.item())
        score += 1
        name_list.remove(answer)
    title = f"{score}/50 guesses correct"
    is_guess_on += 1

new_frame = pandas.DataFrame(name_list, columns=["Names"])
new_frame.to_csv("states_to_learn.csv")
