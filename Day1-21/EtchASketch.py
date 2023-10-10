''' use event listeners to perform sketching on the screen
1. W = forwards
2. S = backwards
3. A = Counter-clockwise
4. D = Clockwise
5. C = Clear drawing'''
from turtle import Turtle, Screen

def move_for():
    tim.forward(30)
def move_bw():
    tim.backward(50)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
def counter_c():
    tim.left(90)
    tim.forward(30)
def clock_c():
    nh = tim.heading() - 10
    tim.setheading(nh)

tim = Turtle()
screen = Screen()

tim.shape("arrow")

tim.color("black", "yellow")
screen.listen()
screen.onkey(move_for, "W")
screen.onkey(move_bw, "S")
screen.onkey(counter_c, "A")
screen.onkey(clock_c, "D")
screen.onkey(clear, "C")


screen.exitonclick()


