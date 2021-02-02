import turtle as t
from game_tools import Paddles, Ball
from scoreboard import Scoreboard
import time


# setup screen
screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
# turn animation off
screen.tracer(0)

#ask players for name

name1 = screen.textinput(title='Player 1',
                         prompt=' Enter player 1 name:')

name2 = screen.textinput(title='Player 2',
                         prompt=' Enter player 2 name:')


# show score board
score_board = Scoreboard()
score_board.player_names(name1, name2)
score_board.update_board()

# set up player paddles
# player one
paddle1 = Paddles()
paddle1.goto(350, 0)
print(paddle1.position())
# player two
paddle2 = Paddles()
paddle2.goto(-350, 0)

# control paddles
screen.listen()
screen.onkeypress(paddle1.move_up, 'Up')
screen.onkeypress(paddle1.move_down, 'Down')

screen.onkeypress(paddle2.move_up, 'w')
screen.onkeypress(paddle2.move_down, 's')
screen.update()


#create ball on screen
ball = Ball()
score_board.count_down()
screen.update()



game_on = True
while game_on:
    screen.update()
    time.sleep(0.04)
    ball.move()

    # detect collision with upper and lower boundaries
    if ball.ycor() >= 289 or ball.ycor() <= -289:
        ball.bounce_wall()

    # detect collision with paddle
    if ball.distance(paddle1) < 45 and ball.xcor() > 330:
        ball.bounce_paddle()
        ball.increase_speed()
    elif ball.distance(paddle2) < 45 and ball.xcor() < -330:
        ball.bounce_paddle()
        ball.increase_speed()

    # detect when ball is out of bounds
    if ball.xcor() > 430:
        ball.ball_reset()
        screen.update()
        # player 2 scored
        score_board.scored('player_2')
        score_board.update_board()
        time.sleep(0.18)

    elif ball.xcor() < -435:
        ball.ball_reset()
        screen.update()
        # player 1 scored
        score_board.scored('player_1')
        score_board.update_board()
        time.sleep(0.18)


screen.exitonclick()