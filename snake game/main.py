from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

s=Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Snake Game")
s.tracer(0)

snake = Snake()
food = Food()
score = Score()

s.listen()
s.onkey(key="w", fun=snake.up)
s.onkey(key="a", fun=snake.left)
s.onkey(key="s", fun=snake.down)
s.onkey(key="d", fun=snake.right)

game_on = True

while game_on:
    s.update()
    time.sleep(0.1)

    snake.move()

    #collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    #collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295 :
        game_on = False
        score.game_over()

    #collision with tail
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on = False
            score.game_over()



s.exitonclick()
