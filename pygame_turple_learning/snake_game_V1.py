# setup
from turtle import Turtle, Screen
import random
import color_lib
playing = False
dan = Turtle()
dan.shape("turtle")
screen = Screen()
screen.bgcolor("#F5F0E0")
screen.screensize(50, 50)
dan.penup()
trail = []
segments = []
delay = 2

# makes the snake
food = Turtle()
food.penup()
food.hideturtle()
food.shape("circle")

# makes the bourder
wall = Turtle()
wall.speed(0)
wall.hideturtle()
wall.penup()
wall.setpos(-200, -200)
wall.pendown()
for i in range(4):
    wall.forward(400)
    wall.left(90)


# Limit trail size so it's only as long as needed
if len(trail) > len(segments) * delay:
    trail.pop(0)


# Move each segment to its corresponding trail position
for i, segment in enumerate(segments):
    if len(trail) > (i + 1) * delay:
        segment.setpos(trail[-(i + 1) * delay])


# makes a new block that can be made to follow the snake using the segment list
def grow_snake():
    new_segment = Turtle()
    new_segment.hideturtle()
    new_segment.shape("square")
    new_segment.color("black")
    new_segment.penup()
    segments.append(new_segment)


# if legal turns up
def turn_up():
    if not dan.heading() == 270:
        dan.setheading(90)


# if legal turns down
def turn_down():
    if not dan.heading() == 90:
        dan.setheading(270)


# if legal turns left
def turn_left():
    if not dan.heading() == 0:
        dan.setheading(180)


# if legal turns right
def turn_right():
    if not dan.heading() == 180:
        dan.setheading(0)


# resets your position
def reset():
    dan.reset()
    dan.penup()


# shuts it all down
def closing():
    screen.bye()


# starts game loop
def game_start():
    global playing
    playing = True
    game_loop()

# the game play


def game_loop():
    if playing:
        for i in segments[:-1]:
            # show the block that just got moved behind player
            i.showturtle()

        # keeps us moving and keeps track
        dan.forward(20)
        trail.append(dan.pos())

        # Keep trail the right length
        if len(trail) > len(segments) * delay:
            trail.pop(0)

        # Move each body segment
        for i, segment in enumerate(segments):
            if len(trail) > (i + 1) * delay:
                segment.setpos(trail[-(i + 1) * delay])

        # Food collision
        if dan.distance(food) < 15:
            set_food()
            grow_snake()

        # Wall collision
        x, y = dan.pos()
        if x < -200 or x > 200 or y < -200 or y > 200:
            closing()

        screen.ontimer(game_loop, 100)


# keybinds
screen.listen()
screen.onkey(turn_up, "w")
screen.onkey(turn_down, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(reset, "r")
screen.onkey(closing, "c")
screen.onkey(game_start, "space")


# randomly places food
def set_food():
    food.hideturtle()
    x = random.choice(range(-200, 200))
    y = random.choice(range(-200, 200))
    food.setpos(x, y)
    food.showturtle()
set_food()

screen.mainloop()
