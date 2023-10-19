from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.turtlesize(stretch_wid=6, stretch_len=1.3)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
    def move(self):
        self.setposition(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def bounce_y(self):
        self.y_move *= -1
        self.move()

    def bounce_x(self):
        self.x_move *= -1
        self.move()

    def reset(self):
        self.setposition(0,0)
        self.x_move *= -1