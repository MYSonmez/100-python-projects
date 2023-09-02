from turtle import Turtle, Screen

kusi = Turtle()

print(kusi)
kusi.speed(1)
for n in range(1,10):
    kusi.shape("turtle")
    kusi.color("#A8A196")
    kusi.fillcolor("yellow")
    kusi.right(60)
    kusi.setpos((50,100))
    print(kusi.position())
    kusi.right(30)
    kusi.setpos((50,0))
    kusi.right(90)
    kusi.setpos((0,0))
    kusi.right(9)


my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
