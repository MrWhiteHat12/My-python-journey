from turtle import Turtle, Screen
import random
import color_lib


dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
# dan.hideturtle()
screen.screensize(50, 50)


turn = 360
num_of_turn = 3
value_of_turn = turn // num_of_turn
distance = 50
dan.width(15)

for i in range(5):
    color_lib.make_mod_color("#F5F0E0", 50)
    dan.pencolor(random.choice(color_lib.mod_color))
    for i in range(num_of_turn):
        dan.forward(distance)
        dan.left(value_of_turn)
        dan.forward(distance)
    num_of_turn += 1
    value_of_turn = turn // num_of_turn

screen.exitonclick()
