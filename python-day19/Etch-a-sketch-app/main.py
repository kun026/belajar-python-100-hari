"""
Higher order function => function yang memanggil function lain dan function yang di panggila dinamakan callback.
"""

from turtle import Turtle, Screen

loreng = Turtle()
screen = Screen()

def move_forwards():
    loreng.fd(10)

def move_backwards():
    loreng.backward(10)

def turn_right():
    loreng.right(10)

def turn_left():
    loreng.left(10)

def clear_sketch():
    loreng.penup()
    loreng.home()
    loreng.clear()
    loreng.pendown()

screen.onkey(fun=move_forwards, key="Up")
screen.onkey(fun=move_backwards, key="Down")
screen.onkey(fun=turn_left, key="Left")
screen.onkey(fun=turn_right, key="Right")

screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=turn_right, key="d")

screen.onkey(fun=clear_sketch, key='c')

screen.listen()

screen.exitonclick()