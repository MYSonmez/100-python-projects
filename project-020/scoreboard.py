from turtle import Turtle

ALIGAMENT = "center"
FONT = ("Arial", 16, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("blue")
        self.penup()
        self.goto(0, 264)
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f"Score = {self.score}", move=False, align=ALIGAMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", move=False, align="center", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()
