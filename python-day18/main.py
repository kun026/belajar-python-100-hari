# Import module python
# import random

# from random import random, choice

# General import (tetai ini sangat jarang dilakukan oleh pengguna python)
# from random import *

# aliasing module
# import random as r
# r.randint(0, 10)

import turtle as t
import random

loreng = t.Turtle()
screen = t.Screen()
# loreng.shape('turtle')
# loreng.color('blue')

## Turtle challenge 2
# for _ in range(10):
#     loreng.pendown()
#     loreng.forward(10)
#     loreng.penup()
#     loreng.forward(10)

## Turtle challenge 3
# t.colormode(255)
# for i in range(3, 11):
#     loreng.pencolor(random.randint(0, 255), randint(0, 255), randint(0, 255))
#     for _ in range(i):
#         loreng.pendown()
#         loreng.forward(100)
#         loreng.right(360 / i)

## Turtle challenge 4
# directions = [0, 90, 180, 270]
# t.colormode(255)
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)

# loreng.pensize(10)
# loreng.speed(0)
# for _ in range(500):
#     loreng.color(random_color())
#     loreng.forward(30)
#     loreng.setheading(random.choice(directions))

## Turtle challenge 5 Spirograph
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g , b)

loreng.speed(0)
for i in range(0, 360, 5):
    loreng.color(random_color())
    loreng.setheading(i)
    loreng.circle(100)



screen.exitonclick()