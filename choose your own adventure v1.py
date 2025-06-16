alive = True
going_to_die = False
print("Hello adventurer \nin your following adventure you will be forced to travel a dangerous path\nalways choosing between options that will either lead to your demise or victory")
print("you come upon a cross road the left path covered in a thick fog\nthe right having a design that looks no different from the land you've already walked")

choice = input("do you choose to go left or right? ")

if choice == ("right"):
    print("you walk for another hour before coming upon a lake.")
    choice = input(
        "There's an island in the middle of the lake. \nType 'wait' to wait for a boat. Type 'swim' to swim across? ")
    if choice == ("wait"):
        print("after two days of waiting a boat comes up and takes you across the lake to the island")
        print("as you reach the island you find three doors, one red, one yellow, and one blue.")
        choice = input("which door do you choose(only write the color)? ")
        if choice == ("yellow"):
            print("as the yellow door opens a glisening light shoots out\ninside holding what can only be described as a gem of pure beauty your goal from the start")
        elif choice == ("blue"):
            going_to_die = True
            print("the veiw behind the door is gorgeous\nwhile you had already hit the number of days this jorney is supposed to take you still deside to keep pushing")
            print("after a day of looking you deside you must choose a place to sleep you can either, sleep in a tree, in a cave, or set up you tent")
            choice = input("where will you sleep? ")
            if going_to_die == True and choice == ("tent") or choice == ("cave"):
                print("in the night a bear comes upon you")
                alive = False
            elif going_to_die == True:
                print(
                    "in the night yout hand slips leading you to find yourself falling to your death")
                alive = False
        else:
            going_to_die = True
            if going_to_die == True:
                print(
                    "the land past the door is nothing but a firery hellscape and the heat burns you to a crisp")
                alive = False
    else:
        going_to_die = True
        if going_to_die == True:
            alive = False
            print("you find yourself swimming through a substance thick as syrup\nas you reach the halfway point you loose all streagth to swim and drown")
else:
    going_to_die = True
    print("as you travel down the road a fog starts to close in and breathing becomes harder")
    print("suddenly you collapse your head spinning")
    if going_to_die == True:
        alive = False
        print("you have perrished")

if alive == True:
    print("congrants you win")
elif alive == False:
    print("GAME OVER")
else:
    print("sorry but an error has accured")