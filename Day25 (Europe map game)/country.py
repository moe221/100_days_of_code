from turtle import Turtle
import pandas as pd

df = pd.read_excel('Data/countries_x_y(clean).xlsx')


class Country:
    def __init__(self):
        self.country_names = {}
        self.create_countries()

    def create_countries(self):
        for countries in df['country'].values:
            country = Turtle(shape='circle')
            country.pu()
            country.color('red')
            country.hideturtle()
            country.shapesize(0.4, 0.4)
            x_cor = df[df['country'] == countries]['x']
            y_cor = df[df['country'] == countries]['y']
            country.goto(int(x_cor), int(y_cor))
            self.country_names[countries] = country

    def show_country(self, answer):
        name_of_country = self.country_names[answer]
        name_of_country.color('white')
        name_of_country.write(answer, align='center', font=('arial', 10,'bold'))
        self.country_names.pop(answer)

