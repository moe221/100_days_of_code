# class for snake related functions
import turtle as t

START_X = 0
STEP_DISTANCE = 20
SNAKE_SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.parts = []
        self.make_snake()

    def make_snake(self, startX=START_X):
        for i in range(SNAKE_SIZE):
            body_part = t.Turtle(shape='square')
            body_part.turtlesize(1, 1)
            body_part.color('white')
            body_part.pu()
            body_part.setx(x=startX)
            body_part.sety(y=0)
            startX -= 20
            self.parts.append(body_part)

    def move(self):
        for i in range(len(self.parts) - 1, 0, -1):
            self.parts[i].goto(self.parts[i - 1].position())
        self.parts[0].forward(STEP_DISTANCE)

    def up(self):
        if self.parts[0].heading() != DOWN:
            self.parts[0].setheading(UP)

    def down(self):
        if self.parts[0].heading() != UP:
            self.parts[0].setheading(DOWN)

    def left(self):
        if self.parts[0].heading() != RIGHT:
            self.parts[0].setheading(LEFT)

    def right(self):
        if self.parts[0].heading() != LEFT:
            self.parts[0].setheading(RIGHT)

    def grow(self):
        new_part = t.Turtle(shape='square')
        new_part.turtlesize(1, 1)
        new_part.color('white')
        new_part.pu()
        new_x = self.parts[-1].xcor() -20
        new_y = self.parts[-1].ycor() -20
        new_position = (new_x, new_y)
        new_part.goto(new_position)
        self.parts.append(new_part)

    def reset_snake(self):
        for part in self.parts[3::]:
            part.hideturtle()
        self.parts = self.parts[:3]
        self.parts[0].goto(x=0, y=0)