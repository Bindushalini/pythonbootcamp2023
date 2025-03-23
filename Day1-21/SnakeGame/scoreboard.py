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
        self.highscore = int(self.read_data_file())
        self.hideturtle()
        self.display_score()

    def display_score(self):
        self.clear()
        self.setposition(0, 280)
        self.write(f"Score is {self.score} highscore: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setposition(0, 0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", 'w') as fh1:
                fh1.write(str(self.highscore))
        self.score = 0
        self.display_score()

    def update_score(self):
        self.score += 1

    def read_data_file(self):
        with open("data.txt", 'r') as fh:
            return fh.read()
