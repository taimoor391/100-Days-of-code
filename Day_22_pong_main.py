from turtle import Screen
from Paddle import Paddle
from ball import Ball
from Scoreeboard import ScoreBoard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("My Pong Game")
screen.tracer(0)

r_paddle = Paddle(370, 0)
l_paddle = Paddle(-370, 0)
ball = Ball()
score_board=ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:

    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # collision with right paddle
    if ball.xcor() > 330 and ball.distance(r_paddle) < 50 or ball.xcor() < -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # ball goes beyond the paddle
    if ball.xcor() > 350:
        ball.reset_position()
        score_board.l_points()

    if ball.xcor() < -350:
        ball.reset_position()
        score_board.r_points()





screen.exitonclick()
