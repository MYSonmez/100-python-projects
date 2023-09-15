# The Hirst Painting Project

import turtle
import random


turtle.colormode(255)

kusi = turtle.Turtle()
kusi.speed("fastest")
kusi.hideturtle()


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

x = -225
y = -225
for _ in range(10):
    kusi.penup()
    kusi.setpos(x, y)
    y += 50
    for _ in range(10):
        kusi.dot(20, random_color())
        kusi.forward(50)



screen = turtle.Screen()
screen.exitonclick()