from turtle import Turtle, Screen
import random

race_on = False

s=Screen()
s.setup(width=500, height=400)
guess=(s.textinput(title="make a bet", prompt="Who will win the race? Guess the colour")).lower()


colors=["purple", "blue", "green", "yellow", "orange", "red"]
turtle = []

incr = 0
for color in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + incr)
    incr+=50
    turtle.append(new_turtle)

if guess:
    race_on = True

while race_on:
    for t in turtle:

        if t.xcor() > 225:
            race_on = False
            winner_color=t.pencolor()
            if guess == winner_color:
                print(f"you have won!!! {winner_color} is the winner")

            else:
                print(f"you have lost!!! {winner_color} is the winner")

        distance = random.randint(0, 10)
        t.forward(distance)





s.exitonclick()

