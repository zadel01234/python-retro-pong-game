from turtle import Turtle, Screen
import time
import random
from createpaddle import Paddle
from ballmovement import Ball
from pongscoreboard import Score

screen = Screen()
screen.title("Zadel's Pong Game")
screen.setup(800,600)
screen.bgcolor("black")
screen.tracer(0)


left_paddle = Paddle((-360,0))
right_paddle = Paddle((360,0))
ball = Ball()
scores = Score()



screen.listen()
screen.onkey(fun = left_paddle.go_up, key = "w")
screen.onkey(fun = left_paddle.go_down, key = "s")

screen.onkey(fun = right_paddle.go_up, key = "Up")
screen.onkey(fun = right_paddle.go_down, key = "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.faster)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    

    # collision with right_paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        

    # detect miss to count score
    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() < -380:
            scores.awaywin()
        elif ball.xcor() > 380:
            scores.homewin()
        ball.ball_refresh()

    game_is_on = scores.winner()



screen.mainloop()