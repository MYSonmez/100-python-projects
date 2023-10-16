from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.SPEED = [3, 1]

    def move(self):
        self.goto(self.xcor() + self.SPEED[0], self.ycor() + self.SPEED[1])

    def bounce(self, rp, lp):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.SPEED[1] = -self.SPEED[1]
        elif self.xcor() >= 340 or self.xcor() <= -340:
            if self.distance(rp) <= 58 or self.distance(lp) <= 58:
                self.SPEED[0] = -self.SPEED[0]

    def reset_position(self, rp, lp):
        self.goto(0, 0)
        rp.goto(360, 0)
        lp.goto(-360, 0)
