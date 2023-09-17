# Etch-A-Sketch App


import turtle

kusi = turtle.Turtle()
kusi.speed("fastest")


def move_forward():
    kusi.forward(20)


def turn_right():
    kusi.right(10)


def turn_left():
    kusi.left(10)


def move_back():
    kusi.backward(20)


def clear_screen():
    screen.reset()


screen = turtle.Screen()
screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=move_back, key="s")
screen.onkey(fun=clear_screen, key="c")
screen.exitonclick()
