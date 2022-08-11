from turtle import Turtle

FONT = ('Arial', 10, 'normal')


class Country:
    def __init__(self):
        self.countries = []

    def add_country(self, name, x, y):
        new_country = Turtle("turtle")
        new_country.pu()
        new_country.goto(int(x), int(y))
        new_country.hideturtle()
        new_country.write(name, True, "center", FONT)
        self.countries.append(name)

    def already_counted(self, name):
        return name in self.countries
