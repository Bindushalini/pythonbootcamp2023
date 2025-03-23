from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.color("cyan")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.setposition(random.randint(-280, 280), random.randint(-280, 280))


