import time
from turtle import Screen
from car_manager import CarManager
from player import Player

from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(fun=player.move_turtle, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.car_spawning()
    car_manager.move_car()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    #detect successful crossing
    if player.crossing_success():
        player.go_to_starting()
        scoreboard.update_level()
        car_manager.increase_speed()

screen.exitonclick()
