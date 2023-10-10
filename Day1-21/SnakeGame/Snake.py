from turtle import Turtle

SNAKE_DISTANCE = 10
SNAKE_POSITION = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_list = []
        self.build_body()
        self.head = self.snake_list[0]

    def build_body(self):
        x_pos = 0
        for i in range(3):
            self.build(x_pos, 0)
            x_pos -= SNAKE_POSITION

    def build(self, at_x_pos, at_y_pos):
        snake = Turtle()
        snake.shape("square")
        snake.penup()
        snake.resizemode("user")
        snake.shapesize(0.5, 0.5)
        snake.color("white")
        snake.setposition(at_x_pos, at_y_pos)
        self.snake_list.append(snake)

    def move(self):
        for i in range(len(self.snake_list) - 1, 0, -1):
            # time.sleep(0.8)
            self.snake_list[i].setposition(self.snake_list[i - 1].position())
        self.snake_list[0].forward(SNAKE_DISTANCE)
        # self.snake_list[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def extend(self):
        self.build(self.snake_list[-1].xcor(), self.snake_list[-1].ycor())
