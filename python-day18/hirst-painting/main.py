# import colorgram

# colors = colorgram.extract("python-day18/hirst-painting/image.jpg", 30)

# def format_color(colors_list):
#     colors = []
#     for color in colors_list:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         colors.append((r, g , b))
#     return colors

# print(format_color(colors))

import turtle as t
from random import choice

loreng = t.Turtle()
screen = t.Screen()
t.colormode(255)

colors = [(202, 164, 110), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

loreng.hideturtle()
loreng.speed('fastest')

x_cor = -320
y_cor = -260

loreng.goto(x_cor, y_cor)
loreng.clear()

for y in range(10):
    for x in range(10):
        loreng.dot(20, choice(colors))
        loreng.teleport(loreng.xcor() + 50)
    loreng.teleport(x_cor, loreng.ycor() + 50)

screen.exitonclick()