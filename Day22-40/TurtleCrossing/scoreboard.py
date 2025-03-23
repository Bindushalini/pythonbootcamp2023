FONT = ("Courier", 20, "normal")
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.display_scoreboard()

        # self.display_score()

    def display_scoreboard(self):
        self.clear()
        self.goto(-200, 200)
        self.write(f" Level: {self.score}", move=False, align="left", font=FONT)

    def inc_score(self):
        self.score += 1
        self.display_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f" GAME OVER", move=False, align="center", font=FONT)
