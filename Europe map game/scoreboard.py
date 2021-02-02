from turtle import Turtle
import time

TIMER = 300


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color('white')
        self.score = 0
        self.game_time = TIMER
        # file = open('data.txt')
        # self.high_score = int(file.read())
        # file.close()

    # define the countdown func.
    def countdown(self):
        while self.game_time:
            mins, secs = divmod(self.game_time, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            self.goto(0, 0)
            self.write(timer, align='center', font=30)
            self.game_time -= 1
            time.sleep(1)
            self.clear()


