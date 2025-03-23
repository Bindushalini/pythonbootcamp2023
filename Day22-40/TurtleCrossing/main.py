import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
my_turtle = Player()
new_car = CarManager()
screen.listen()
screen.onkey(my_turtle.move_up, "Up")
my_score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    new_car.create_car()
    new_car.move_ahead()
    # check collision
    if new_car.check_collision(my_turtle):
        game_is_on = False
        my_score.game_over()
    #check if reached finish line
    if my_turtle.is_at_finish_line():
        my_turtle.set_position_to_init()
        new_car.increase_speed()
        my_score.inc_score()

screen.exitonclick()

