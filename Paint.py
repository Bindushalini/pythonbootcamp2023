import colorgram as cg
import random
import turtle as t
from turtle import Screen

# colors = cg.extract("./paint.jpg", 30)
# color_list = []
# for c in colors:
#     red = c.rgb.r
#     green = c.rgb.g
#     blue = c.rgb.b
#     new_color = (red, green, blue)
#     color_list.append(new_color)
#
# print(color_list)
color_list = [(222, 152, 103), (233, 237, 240), (128, 172, 199), (221, 130, 149), (221, 73, 90),
              (243, 208, 99), (17, 121, 157), (118, 176, 147), (34, 120, 82), (18, 165, 204), (230, 74, 70),
              (142, 86, 60),
              (116, 85, 102), (162, 209, 162), (13, 169, 120), (171, 183, 219), (177, 154, 75), (213, 222, 213),
              (1, 98, 119),
              (54, 61, 96), (240, 177, 165), (221, 167, 185), (146, 204, 228), (24, 98, 61)]


def get_random_color():
    return random.choice(color_list)


def turn_right(t):
    t.right(90)
    t.penup()
    t.forward(50)
    t.right(90)
    t.forward(50)


def turn_left(t):
    t.left(90)
    t.penup()
    t.forward(50)
    t.left(90)
    t.forward(50)


def draw(tobj):
    for _x in range(10):
        tobj.speed(0)
        tobj.dot(20, get_random_color())
        tobj.penup()
        tobj.forward(50)


tim = t.Turtle()
screen = Screen()

t.colormode(255)
# tim.setx(-400)
tim.penup()
tim.hideturtle()
tim.setposition(-200,300)
tim.pendown()
tim.shape("circle")


for x in range(5):
    draw(tim)
    turn_right(tim)
    draw(tim)
    turn_left(tim)

screen.exitonclick()
