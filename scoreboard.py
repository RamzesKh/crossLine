from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(-280,260)
        self.write(f"SCORE {self.score}", font=FONT)
        self.hideturtle()

    def updateScore(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE {self.score}", font=FONT)
    def reset(self):
        self.score = 0
        self.clear()
        self.write(f"SCORE {self.score}", font=FONT)

