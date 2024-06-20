"""
# function Get mouse click coordinates in Python turtle
import turtle

def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)

turtle.mainloop()
"""

import turtle

screen = turtle.Screen()
screen.title("U.S States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


screen.mainloop()