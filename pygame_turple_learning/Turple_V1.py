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
dan.setposition(-255, -255)


def make_spiral(size_of_dot, backround, too_close):
    color_lib.make_mod_color(backround, too_close)
    inbetween = int(size_of_dot*2.5)
    a = int(495 / (size_of_dot + inbetween / 2) - 1)
    for i in range(3):
        for i in range(a):
            dan.dot(size_of_dot, random.choice(color_lib.mod_color))
            dan.forward(inbetween)
        dan.left(90)
    a -= 1
    for i in range(10):
        for i in range(2):
            for i in range(a):
                dan.dot(size_of_dot, random.choice(color_lib.mod_color))
                dan.forward(inbetween)
            dan.left(90)
        a -= 1
    for i in range(2):
        for i in range(a):
            dan.dot(size_of_dot, random.choice(color_lib.mod_color))
            dan.forward(inbetween)
        dan.left(90)
        a -= 1

    dan.dot(size_of_dot, random.choice(color_lib.mod_color))


how_big = input("how big do you want the dot to be? ")
make_spiral(how_big, "#F5F0E0", 50)

screen.exitonclick()
