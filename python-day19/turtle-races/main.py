from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "blue", "yellow", "green", "purple", "orange"]

y_pos = [-70, -40, -10, 20, 50, 80]

all_turtles = []

for i in range(6):
    t = Turtle("turtle")
    t.penup()
    t.color(colors[i])
    t.goto(x=-230, y=y_pos[i])
    all_turtles.append(t)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.fd(random_distance)


screen.exitonclick()