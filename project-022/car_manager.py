from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        while True:
            self.color(random.choice(COLORS))
            self.shape("square")
            self.setheading(180)
            self.shapesize(1, 2)

    def move_car(self):
        self.forward(MOVE_INCREMENT)