from turtle import Turtle
import time
import random

# create class for paddles
class Paddles(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()

    def move_up(self):
        if self.ycor() <= 235:
            self.sety(self.ycor() + 30)

    def move_down(self):
        if self.ycor() >= -225:
            self.sety(self.ycor() - 30)


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        # self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.speed_x = 10
        self.speed_y = 10

    def move(self):
        self.setx(self.xcor() + self.speed_x)
        self.sety(self.ycor() + self.speed_y)

    def bounce_wall(self):
        self.speed_y *= -1

    def bounce_paddle(self):
        self.speed_x *= -1
        if self.heading() == 180:
            self.setheading(0)
        else:
            self.setheading(180)

    def increase_speed(self):
        self.speed_x *= 1.05
        self.speed_y *= 1.05

    def ball_reset(self):
        self.home()
        if self.speed_x < 0:
            self.speed_x = 10
        else:
            self.speed_x = -10
        self.speed_y = random.choice([-10, 10])
