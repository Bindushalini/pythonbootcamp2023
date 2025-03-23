import time
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_no = random.randint(1,6)
        if random_no == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.turtlesize(0.8, 2.5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.setposition(270, random.randint(-240, 240))
            self.car_list.append(new_car)

    def move_ahead(self):
        for cars in self.car_list:
            cars.backward(self.car_speed)

    def check_collision(self, turtle):
        for car in self.car_list:
            if car.distance(turtle) < 25:
                return True
        return False

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT





