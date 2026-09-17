from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.goto(0, 260)

        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.score = 0
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score

            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()
