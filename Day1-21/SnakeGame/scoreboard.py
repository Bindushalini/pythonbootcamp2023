from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")
BOARD_COLOR = "white"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(BOARD_COLOR)
        self.score = 0
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.setposition(0, 280)
        self.write(f"Score is {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
