from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title(f"{'Pong': ^230}")
screen.tracer(0)

player1 = Paddle((350, 0))
player2 = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player1.move_up, "Up")
screen.onkeypress(player1.move_down, "Down")
screen.onkeypress(player2.move_up, "w")
screen.onkeypress(player2.move_down, "s")


def round():
    scoreboard.write_score()
    ball.goto(0, 0)
    game_on = True
    while game_on:
        screen.update()
        time.sleep(ball.spleep)
        ball.move()

        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.wall_bounce()
        if (ball.distance(player1) < 50 and ball.xcor() > 330) or ball.distance(player2) < 50 and ball.xcor() < -330:
            ball.paddle_bounce()

        if ball.xcor() > 380:
            scoreboard.r_score += 1
            ball.reset_position()
            return round()
        if ball.xcor() < -380:
            scoreboard.l_score += 1
            ball.reset_position()
            return round()


round()

screen.exitonclick()
