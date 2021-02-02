from turtle import Turtle, Screen
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.pu()
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.count = 0
        self.name1 = 'Player 1'
        self.name2 = 'Player 2'

    def scored(self, player):
        if player == 'player_2':
            self.player2_score += 1
        elif player == 'player_1':
            self.player1_score += 1

    def update_board(self):
        self.clear()
        self.goto(100, 200)
        self.write(self.player1_score,
                   align='center',
                   font=('Arial', 20, 'normal'))

        self.goto(100, 235)
        self.write(self.name1,
                   align='center',
                   font=('Arial', 20, 'normal'))

        self.goto(-100, 200)
        self.write(self.player2_score,
                   align='center',
                   font=('Arial', 20, 'normal'))

        self.goto(-100, 235)
        self.write(self.name2,
                   align='center',
                   font=('Arial', 20, 'normal'))

    def player_names(self, name1, name2):
        self.name1 = name1
        self.name2 = name2

    def count_down(self):
        for seconds in range(1, 4):
            self.count +=1
            self.goto(0, 0)
            self.write(self.count,
                       align='center',
                       font=('Arial', 80, 'normal'))
            time.sleep(1)
            self.update_board()

