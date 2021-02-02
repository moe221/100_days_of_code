from turtle import Turtle


class Gameboard(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.hideturtle()
        self.color('white')
        self.score = 0
        file = open('data.txt')
        self.high_score = int(file.read())
        file.close()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=25)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            file = open('data.txt', mode='w')
            file.write(f'{self.high_score}')
            file.close()
        self.score = 0
        self.clear()

    def score_board(self, my_list):
        self.goto(0, 350)
        self.clear()
        self.score = len(my_list) - 3
        self.reset_score()
        self.write(f'YOUR SCORE: {len(my_list) - 3}  HIGH SCORE: {self.high_score}', align='center', font=25)
