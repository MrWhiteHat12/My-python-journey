import random


# a function to deside who wins if error1-4 is printed it happened here
def who_wins(player_choices, computer_choice):
    if player_choices == ("rock"):
        player_choices = int(1)
    elif player_choices == ("paper"):
        player_choices = int(2)
    elif player_choices == ("scissors"):
        player_choices = int(3)
    else:
        print("error1")

    if computer_choice == 1:
        if player_choices == 1:
            print("tie")
        elif player_choices == 2:
            print("you lose")
        elif player_choices == 3:
            print("you win")
        else:
            print("error2")
    elif computer_choice == 2:
        if player_choices == 1:
            print("you lose")
        elif player_choices == 2:
            print("tie")
        elif player_choices == 3:
            print("you win")
        else:
            print("error3")
    elif computer_choice == 3:
        if player_choices == 1:
            print("you win")
        elif player_choices == 2:
            print("you lose")
        elif player_choices == 3:
            print("tie")
        else:
            print("error4")
    else:
        print("error5")


# startup
want_to_play = True
rigged = False  # rig it so computer wins
options = [1, 2, 3]

while want_to_play == True:  # playing loop
    player_choice = input("do you choose rock, paper, or scissors? ")
    computer_choice = random.choice(options)
    if rigged == True:
        print("you lose")
    else:
        who_wins(player_choice, computer_choice)
    want_to_play = False
    continues = input("do you want to play again?(yes, no) ")
    if continues == ("yes"):
        want_to_play = True
    elif continues == ("no"):
        want_to_play = False
print("Good Game")
