from turtle import Turtle, Screen
import random
import color_lib


dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
screen.colormode
dan.hideturtle()
screen.screensize(50, 50)
dan.penup()
dan.setposition(-255, -255)
color_lib.make_mod_color("#F5F0E0", 50)
a = 10
for i in range(17):
    for i in range(3):
        for i in range(a):
            dan.dot(20, random.choice(color_lib.mod_color))
            dan.forward(50)
        dan.left(90)
    a -= 1


screen.exitonclick
