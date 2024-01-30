from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

scoreboard=ScoreBoard()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

ball=Ball()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on=True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    # detect collision with wall
    if ball.ycor()==300 or ball.ycor()==-300:
        ball.bounce_Y()
#  detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() >320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_X()

    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()