import turtle


class Paddle(turtle.Turtle):
    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.setposition(xpos, ypos)
        self.turtlesize(stretch_wid=5,stretch_len=1)
        self.color("white")
        self.penup()

    def up(self):
        self.setposition(self.xcor(), self.ycor() + 20)

    def down(self):
        self.setposition(self.xcor(), self.ycor() - 20)


