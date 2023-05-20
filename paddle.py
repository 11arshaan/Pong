from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, side):
        super().__init__("square")
        self.start_x = 350 if side == "right" else -350
        self.color("white")
        self.setheading(90)
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(self.start_x, 0)
        self.moving = False
        self.movement = 20

    def set_up(self):
        self.movement = 20
        if self.ycor() <= 250:
            self.moving = True

    def set_down(self):
        self.movement = -20
        if self.ycor() >= -250:
            self.moving = True

    def release(self):
        self.moving = False

    def move(self):
        if self.moving and -250 <= self.ycor() <= 250:
            self.goto(self.start_x, self.ycor() + self.movement)
