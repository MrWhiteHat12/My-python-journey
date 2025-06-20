from turtle import Turtle, Screen
import random
import color_lib


dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
screen.screensize(50, 50)


def move_forward():
    dan.forward(10)


def move_backward():
    dan.backward(10)


def turn_left():
    dan.left(15)


def turn_right():
    dan.right(15)


def clearing():
    dan.speed(0)
    pos = dan.position()
    screen.resetscreen()
    dan.penup()
    dan.setposition(pos)
    dan.speed(6)
    dan.pendown()


def up():
    dan.penup()


def down():
    dan.pendown()


# Set up key bindings
screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clearing, "c")
screen.onkey(up, "Up")
screen.onkey(down, "Down")

screen.mainloop()
