from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 200)
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def draw_game_area(self):
        kusi = Turtle()
        kusi.color("white")
        kusi.penup()
        kusi.hideturtle()
        kusi.goto(-400, -300)
        kusi.pendown()
        kusi.goto(400, -300)
        kusi.penup()
        kusi.goto(400, 300)
        kusi.pendown()
        kusi.goto(-400, 300)

    def update_scoreboard(self):
        self.write(
            arg=f"{self.l_score} - {self.r_score}",
            align="center",
            font=("Courier", 50, "normal"),
        )

    def increase_score(self, ball):
        if ball.xcor() > 360:
            self.clear()
            self.l_score += 1
            self.update_scoreboard()

        elif ball.xcor() < -360:
            self.clear()
            self.r_score += 1
            self.update_scoreboard()

    def game_over(self, user):
        self.goto(0, 0)
        self.write(
            arg=user + " won!",
            align="center",
            font=("Courier", 50, "normal"),
        )
