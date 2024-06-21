"""
# function Get mouse click coordinates in Python turtle
import turtle

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
"""

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct",
                                    prompt="Whats's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = {
            "missing state": missing_states
        }

        df = pandas.DataFrame(new_data)
        df.to_csv("state_to_learn.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data.state == answer_state]
        x_cor = state_data.x.item()
        y_cor = state_data.y.item()
        t.teleport(x_cor, y_cor)
        t.write(state_data.state.item())
