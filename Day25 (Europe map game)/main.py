import turtle as t
import pandas as pd
import time
from country import Country
from scoreboard import Scoreboard
from turtle_party import Winner
import threading
import random

df = pd.read_excel('Data/countries_x_y(clean).xlsx')

screen = t.Screen()
screen.setup(width=952, height=790)
screen.title('Europe Countries Game')

# set map
image = 'Images/03-Europe-country-outlines_new.gif'
screen.addshape(image)
t.Turtle().shape(image)

# turn animation off
screen.tracer(0)
country = Country()
screen.tracer(1)

# setup scoreboard
scoreboard = Scoreboard()


def show_all_countries():
    for turtles in list(country.country_names):
        country.show_country(turtles)


# keep asking user for input
def check_answers():
    screen.update()
    num_of_countries = len(country.country_names)
    num_correct_answers = 0

    while len(country.country_names) > 0:
        random_country = random.choice(list(country.country_names))
        country_turtle = country.country_names[random_country]
        country_turtle.getscreen()
        country_turtle.showturtle()
        while True:

            try:
                answer_country = screen.textinput(title=f'{num_correct_answers}/{num_of_countries} Guess a country',
                                                  prompt="What's this country?").title()
            except AttributeError:
                continue
            else:
                if answer_country == random_country:
                    country_turtle.hideturtle()
                    num_correct_answers += 1
                    country.show_country(answer_country)
                    break
                elif answer_country == 'Give Up':
                    show_all_countries()
                    break

                else:
                    country_turtle.hideturtle()
                    break


check_answers()

# generate turtles randomly
screen.tracer(0)
winner = Winner()
while True:
    time.sleep(0.05)
    winner.make_turtles()
    winner.move()
    winner.remove_turtles()
    screen.update()

screen.exitonclick()
