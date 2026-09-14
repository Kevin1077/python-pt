from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()
