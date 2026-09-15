from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s= Screen()

s.setup(width=800, height=600)
s.bgcolor("black")
s.title("Pong")
s.tracer(0)


paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


s.listen()

s.onkey(key="Up", fun=paddle_r.upward)
s.onkey(key="Down", fun=paddle_r.down)
s.onkey(key="w", fun=paddle_l.upward)
s.onkey(key="s", fun=paddle_l.down)


game_is_on = True

while game_is_on:
    time.sleep(ball.ball_speed)
    s.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    #if paddle_r misses the ball
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()


    #if paddle_l misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()




s.exitonclick()
