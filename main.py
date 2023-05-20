from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

scoreboard = Scoreboard()

ball = Ball()
right_paddle = Paddle("right")
left_paddle = Paddle("left")

# Controls
screen.listen()

# Right Paddle Controls
screen.onkeypress(right_paddle.set_up, "Up")
screen.onkeyrelease(right_paddle.release, "Up")
screen.onkeypress(right_paddle.set_down, "Down")
screen.onkeyrelease(right_paddle.release, "Down")

# Left Paddle Controls
screen.onkeypress(left_paddle.set_up, "w")
screen.onkeyrelease(left_paddle.release, "w")
screen.onkeypress(left_paddle.set_down, "s")
screen.onkeyrelease(left_paddle.release, "s")

# Toggle Draw Path
screen.onkey(ball.set_pen, "space")

game_on = True

while game_on:
    screen.update()
    time.sleep(0.032)
    ball.move()
    ball.check_collision(scoreboard)
    ball.check_paddle(left_paddle, right_paddle)
    moves = [right_paddle.move, left_paddle.move]
    random.shuffle(moves)
    for move in moves:
        move()

screen.exitonclick()
