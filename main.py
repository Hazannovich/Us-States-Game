import time

import pandas
import turtle
from country import Country
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S States Game")
screen.setup(725, 491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()
game_is_on = True
countries = Country()
scoreboard = Scoreboard()
while game_is_on:
    user_input = screen.textinput(f"{scoreboard.score}/50 Correct States", "what's another state's name?").title()
    if not user_input or user_input == "Exit":
        user_input = screen.textinput("GoodBye", "Are you sure you want to quit?(yes/no)").title()
        if user_input == "Yes":
            game_is_on = False
            scoreboard.game_over()
            missing_states = [state for state in all_states if not countries.already_counted(state)]
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_to_learn.csv")
            time.sleep(2)
    elif user_input in all_states:
        state = states_data[states_data.state == user_input]
        name = state.state.to_string(header=False, index=False)
        x_cor = state.x.to_string(header=False, index=False)
        y_cor = state.y.to_string(header=False, index=False)
        if not countries.already_counted(name):
            countries.add_country(name, x_cor, y_cor)
            scoreboard.update_score()
    if scoreboard.score == 50:
        scoreboard.congrats()
        game_is_on = False
        time.sleep(2)
    user_input = ""


