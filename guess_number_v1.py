import random
import keyboard_lib
trys = 0
mode = input("whould you like to play on easy(1) or hard(2) mode? ")
number = random.choice(range(1, 100))
mode = int(mode)
print(number)
want_to_play = True


if mode == 1:
    print("ok you have 10 guesses")
    trys = 10
elif mode == 2:
    print("ok you have 5 guesses")
    trys = 5
else:
    print("invalid input")

while want_to_play == True:
    while trys > 0:
        guess = input("what is your guess? ")
        guess = int(guess)
        if guess > number:
            print("too high")
            trys -= 1
        elif guess < number:
            print("too low")
            trys -= 1
        elif guess == number:
            trys = 0

    if guess == number:
        print(f"good job you did it the number was {number}")
    elif not guess == number:
        print(f"bummer you ran out of guesses the number was {number}")
    else:
        print(f"an error has accured the number was {number}")
    redo = input("do you want to play again y/n: ")
    if redo == ("n"):
        want_to_play = False

print("bummer lets play again sometime")
