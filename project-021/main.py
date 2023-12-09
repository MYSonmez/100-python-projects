from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=1.0, height=1.0)
screen.bgcolor("black")
screen.title("Pong!")
screen.tracer(0)
screen.listen()

scoreboard = Scoreboard()
scoreboard.draw_game_area()
ball = Ball()
r_paddle = Paddle(360, 0)
l_paddle = Paddle(-360, 0)


screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    # acclerate the ball
    if ball.xcor() >= 340 or ball.xcor() <= -340:
         ball.SPEED[0] *= 1.03
         ball.SPEED[1] *= 1.03
         ball.random_color()
    
    # goal case
    if ball.xcor() > 380 or ball.xcor() < -380:
        scoreboard.increase_score(ball)
        ball.reset_position(rp=r_paddle, lp=l_paddle)
        ball.SPEED = [3,1]
    screen.update()
    time.sleep(0.008)
    ball.move()
    ball.bounce(rp=r_paddle, lp=l_paddle)
    if scoreboard.l_score == 5:
        scoreboard.game_over(user="User_1")
        game_is_on = False
        ball.hideturtle()
    if scoreboard.r_score == 5:
        scoreboard.game_over(user="User_2")
        game_is_on = False
        ball.hideturtle()


screen.exitonclick()
