from turtle import Turtle
import math


class Ball(Turtle):

    def __init__(self):
        super().__init__("circle")
        self.color("white")
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.side = "right"
        self.is_pen_down = False

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.goto(new_x, new_y)
        if new_x >= 0:
            self.side = "right"
        elif new_x < 0:
            self.side = "left"

    def set_pen(self):
        if self.is_pen_down:
            self.penup()
            self.is_pen_down = False
        else:
            self.pendown()
            self.is_pen_down = True

    def check_collision(self, scoreboard):
        if self.ycor() >= 290 or self.ycor() <= -290:
            self.bounce("wall")
        if self.xcor() >= 390:
            scoreboard.l_point()
            self.reset()
        elif self.xcor() <= - 390:
            scoreboard.r_point()
            self.reset()

    def check_paddle(self, left_paddle, right_paddle):
        if self.distance(left_paddle) < 50 and self.xcor() <= -320:
            self.bounce("paddle_left")
        if self.distance(right_paddle) < 50 and self.xcor() >= 320:
            self.bounce("paddle_right")

    def bounce(self, direction):
        if direction == "wall":
            self.move_y *= -1
        elif direction == "paddle_left":
            self.move_x = abs(self.move_x)
            self.move_y *= -1
        elif direction == "paddle_right":
            self.move_x = abs(self.move_x) * -1
            self.move_y *= -1

    def reset(self):
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.side = "right"
