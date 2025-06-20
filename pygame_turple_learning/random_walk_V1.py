# import
from turtle import Turtle, Screen
import random
import color_lib


# setup
steps = input("how many steps should it go? ")
dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
dan.hideturtle()
screen.screensize(50, 50)
length_of_step = 20
turn_values = [45, 90, 170, 270, 370]
direction = ["left", "right"]
direction_cmd = (random.choice(direction))
dan.width(10)


def dan_direction(turtle_name):
    direction_cmd = (random.choice(direction))
    if direction_cmd == "left":
        turtle_name.left(random.choice(turn_values))
    else:
        turtle_name.right(random.choice(turn_values))


# walking
for i in range(int(steps)):
    color_lib.make_mod_color("#F5F0E0", 10)
    dan.pencolor(random.choice(color_lib.mod_color))
    dan_direction(dan)
    dan.forward(length_of_step)

screen.exitonclick()
