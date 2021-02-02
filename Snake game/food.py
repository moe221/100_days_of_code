import turtle as t
import random


class Food(t.Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.shapesize(stretch_len=0.50, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        random_x = random.randrange(-380, 380, 20)
        random_y = random.randrange(-380, 380, 20)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-380, 380)
        random_y = random.randint(-380, 380)
        self.goto(random_x, random_y)
