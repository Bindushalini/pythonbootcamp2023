from turtle import Screen
import time
import Snake
import Food
from scoreboard import ScoreBoard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("SnakeGame")
my_screen.tracer(0)
snake = Snake.Snake()
food = Food.Food()
sb = ScoreBoard()
my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")


is_game_on = True


while is_game_on:
    my_screen.update()
    time.sleep(snake.get_speed())
    snake.move()
    sb.display_score()
    # detect collision from food
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        sb.update_score()
        if sb.score % 5 == 0:  # fasten the speed after 5 turns
            snake.set_speed()
    # detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        sb.reset_score()
        snake.reset_snake()
    # detect collision with tail
    for snake_body in snake.snake_list[1:]:
        if snake.head.distance(snake_body) < 5:
            sb.reset_score()
            snake.reset_snake()
my_screen.exitonclick()
