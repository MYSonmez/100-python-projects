from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.move_speed = MOVE_INCREMENT
        self.color(random.choice(COLORS))
        self.penup()
        self.shape("square")
        self.goto(random.randint(-260, 300), random.randint(-3, 4) * 60)
        self.setheading(180)
        self.shapesize(1, 2)

    def move_car(self):
        self.forward(self.move_speed)
