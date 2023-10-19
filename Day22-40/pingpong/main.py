from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.bgcolor("black")
my_screen.title("PingPong")
my_screen.tracer(0)

r_paddle = Paddle(380, 0)
l_paddle = Paddle(-385, 0)

my_screen.listen()
my_screen.onkey(l_paddle.up, "Up")
my_screen.onkey(l_paddle.down, "Down")
my_screen.onkey(r_paddle.up, "Left")
my_screen.onkey(r_paddle.down, "Right")
new_ball = Ball()
my_score = ScoreBoard()
is_game_on = True
sleep_amount = 0.005
sleep_time = 0.06
while is_game_on:
    time.sleep(sleep_time)
    my_screen.update()
    new_ball.move()
    # Detect collision with top and bottom wall
    if new_ball.ycor() >= 295 or new_ball.ycor() <= -295:
        new_ball.bounce_y()
    # Detect collision with paddle
    if (r_paddle.distance(new_ball) < 40 and new_ball.xcor() > 340 or l_paddle.distance(new_ball) < 40
            and new_ball.xcor() < -340):
        new_ball.bounce_x()
        sleep_time -= sleep_amount
    # out of the screen
    if new_ball.xcor() >= 400:
        new_ball.reset()
        my_score.lpoint()
        sleep_time = 0.06
    if new_ball.xcor() <= -400:
        new_ball.reset()
        my_score.rpoint()
        sleep_time = 0.06

my_screen.exitonclick()
