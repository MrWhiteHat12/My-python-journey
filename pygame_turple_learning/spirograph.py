from turtle import Turtle, Screen
import random
import color_lib


dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
dan.hideturtle()
screen.screensize(50, 50)
number_of_circles = 20
dan.speed("fastest")

for i in range(number_of_circles+2):
    color_lib.make_mod_color("#F5F0E0", 100)
    dan.pencolor(random.choice(color_lib.mod_color))
    dan.circle(50, 360)
    dan.left(360 // number_of_circles)

screen.exitonclick()
