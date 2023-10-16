import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

kusi = Player()
screen.listen()
screen.onkey(kusi.move, "Up")

scoreboard = Scoreboard()

cars = []

for _ in range(20):
    new_car = CarManager()
    cars.append(new_car)

game_is_on = True
while game_is_on:
    for car in cars:
        car.move_car()
        if car.xcor() < -300:
            car.goto(random.randint(300, 400), random.randint(-3, 4) * 60)

        if kusi.ycor() > 280:
            for car in cars:
                car.move_speed += 2
            kusi.reset_player_pos()
            scoreboard.level += 1
            scoreboard.update_scoreboard()

        if kusi.distance(car) < 25:
            kusi.pencolor("red")
            crushed_car = car

            for car in cars:
                if car != crushed_car:
                    car.hideturtle()

            scoreboard.game_over()
            game_is_on = False

    time.sleep(0.03)
    screen.update()

screen.exitonclick()
