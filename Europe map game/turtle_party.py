from turtle import Turtle
import random
import time

COLORS = ['red', 'yellow', 'blue', 'brown', 'orange', 'green', 'violet', 'black',
          'white', 'indigo', 'gray']

STARTING_MOVE_DISTANCE = 10
T_POSITIONS_Y = list(x for x in range(400, 410, 25))
T_POSITIONS_X = list(x for x in range(-500, 500, 10))


class Winner:
    def __init__(self):
        self.turtle_list = []
        self.speed = STARTING_MOVE_DISTANCE

    def make_turtles(self):
        turts = Turtle()
        turts.pu()
        turts.shape('turtle')
        turts.setheading(270)
        turts.shapesize(stretch_wid=0.7, stretch_len=0.7)
        turts.color(random.choice(COLORS))
        rand_x = random.choice(T_POSITIONS_X)
        rand_y = random.choice(T_POSITIONS_Y)
        turts.goto(rand_x, rand_y)
        self.turtle_list.append(turts)

    def move(self):
        for turtles in self.turtle_list:
            turtles.sety(turtles.ycor() - self.speed)

    def remove_turtles(self):
        for i in range(len(self.turtle_list)):
            if self.turtle_list[i].ycor() < -400:
                self.turtle_list[i].ht()
                self.turtle_list.pop(i)
                break
