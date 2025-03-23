import turtle as t
import random
from turtle import Screen
import math
def draw_square(turtleobj):
    turtleobj.forward(100)
    turtleobj.right(90)


def draw_shape(tobj, no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        tobj.forward(100)
        tobj.right(angle)


def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


t1_turtle = t.Turtle()
my_screen = Screen()
print(my_screen.colormode(255))
t1_turtle.shape("turtle")
t1_turtle.color("black", "yellow")
# for i in range(4):
#     draw_square(t1_turtle)
# t1_turtle.left(180)
# for _ in range(50):
#     t1_turtle.forward(10)
#     t1_turtle.penup()
#     t1_turtle.forward(10)
#     t1_turtle.pendown()
# color_names = ["medium blue", "green yellow", "coral", "orange", "dark cyan", "pale green"]
#
# t1_turtle.penup()
# t1_turtle.setposition(-10,120)
# t1_turtle.pendown()
# for i in range(3, 11):
#     t1_turtle.pencolor(random.choice(color_names))
#     draw_shape(t1_turtle, i)

# direction = [0, 90, 180, 270]
# t1_turtle.width(10)
#
# draw = 1
# while draw <= 100:
#     t1_turtle.speed(10)
#     t1_turtle.color(random_color())
#     t1_turtle.forward((random.randint(20, 50)))
#     random_direction = random.choice(direction)
#     t1_turtle.setheading(random_direction)
#     draw += 1

# spirograpgh
t1_turtle.width(2)
t1_turtle.shape("circle")
t1_turtle.shapesize(0.3, 0.3, 0.1)
for x in range(math.floor(360/5)):
    print(t1_turtle.heading())
    t1_turtle.speed(0)
    # print(t1_turtle.shapesize())
    t1_turtle.setheading(t1_turtle.heading()+5)
    t1_turtle.color(random_color())
    t1_turtle.circle(100.0, 360)