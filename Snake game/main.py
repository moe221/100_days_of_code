import turtle as t
import time
from snake import Snake
from food import Food
from gameboard import Gameboard

# setup screen using turtle graphics
screen = t.Screen()
screen.setup(width=800, height=800)
screen.bgcolor('black')
screen.title('Snake Game')
# turn animation off
screen.tracer(0)

snake = Snake()
food = Food()

# controlling snake
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

screen.update()
game_board = Gameboard()

game_on = True
game_over = False
while game_on:
    screen.listen()
    screen.update()
    # set snake speed
    time.sleep(0.1)
    snake.move()

    # detect food
    if snake.parts[0].distance(food) < 17:
        snake.grow()
        food.refresh()

    # detect walls
    if snake.parts[0].xcor() > 399 or snake.parts[0].xcor() < -399:
        game_over = True

    elif snake.parts[0].ycor() > 399 or snake.parts[0].ycor() < -399:
        game_over = True

    # detect self
    for num in range(1, len(snake.parts)):
        if snake.parts[0].distance(snake.parts[num]) < 10:
            game_over = True

    if game_over:
        game_board.score_board(my_list=snake.parts)
        game_board.game_over()
        play_again = screen.textinput(title='You lost!',
                                      prompt=' Start a new game? y/n')
        # check if user would like to replay
        if play_again == 'y':
            snake.reset_snake()
            game_board.clear()
            game_over = False
        else:
            game_on = False
