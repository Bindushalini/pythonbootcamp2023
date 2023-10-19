from turtle import Turtle
FONT = ("Arial", 50, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.display_scoreboard()

        # self.display_score()

    def display_scoreboard(self):
        self.clear()
        self.goto(-80, 230)
        self.write(f" {self.l_score}", move=False, align="left", font=FONT)
        self.goto(80, 230)
        self.write(f"{self.r_score}", move=False, align="right", font=FONT)

    def lpoint(self):
        self.l_score+=1
        self.display_scoreboard()

    def rpoint(self):
        self.r_score+=1
        self.display_scoreboard()


