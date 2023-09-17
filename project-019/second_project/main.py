# Turtle Race

from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["red", "blue", "orange", "yellow", "green", "purple"]
red_turtle_y_coordinate = -105

all_turtles = []

for color in colors:
    kusi = Turtle(shape="turtle")
    kusi.speed(2)
    kusi.color(color)
    kusi.penup()
    red_turtle_y_coordinate += 30
    kusi.goto(-230, red_turtle_y_coordinate)
    all_turtles.append(kusi)

user_bet = screen.textinput(
    title="Make your bet", prompt="Who will win this race? Enter a color: "
)

race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        random_distance = random.randint(1, 8)
        turtle.forward(random_distance)

        if turtle.xcor() >= 225:
            race_is_on = False
            winner_color = turtle.fillcolor()

            if winner_color == user_bet:
                print(f"You won! The {winner_color} turtle is the winner.")

            else:
                print(f"You Lose :( The {winner_color} turtle is the winner.")

screen.exitonclick()
