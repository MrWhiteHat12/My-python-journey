from turtle import Turtle, Screen
import random
import color_lib


dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
dan.hideturtle()
screen.screensize(50, 50)
dan.penup()


def make_grid(size_of_dot, backround, too_close):
    left = True
    color_lib.make_mod_color(backround, too_close)
    dan.setposition(-255, -255)
    inbetween = int(size_of_dot*2.5)
    raises = -255
    a = int(495 / (size_of_dot + inbetween / 2)-1)
    for i in range(a+1):
        dan.setheading(0)
        for i in range(a):
            dan.dot(size_of_dot, random.choice(color_lib.mod_color))
            dan.forward(inbetween)
        dan.dot(size_of_dot, random.choice(color_lib.mod_color))
        dan.setx(-255)
        raises += inbetween
        dan.sety(raises)


make_grid(35, "#F5F0E0", 200)

screen.exitonclick()
