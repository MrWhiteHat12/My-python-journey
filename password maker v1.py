# password generator that will pick random characters to make a password that is as long as you need
import random
password_length = input(
    "how long does the password need to be (only add the number): ")
options = [1, 2, 3, 4]
numbers = list(range(10))
misc = ['!', '@', '#', '$', '%', '^', '&', '*',
        '(', ')', '{', '}', '[', ']', "'", '"', ';', ':', '_', '-', '+', '=', ',', '<', '.', '>', '|', "\\", '`', '~']
letters = ['q', 'w', 'e', 'i', 'r', 't', 'y', 'u', 'o', 'p', 'l', 'k',
           'j', 'h', 'g', 'f', 'd', 's', 'a', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
uppercase = ["A", "S", "D", "F", "G", "H", "J", "K", "L", "Q", "W", "E",
             "R", "T", "Y", "U", "I", "O", "P", "Z", "X", "C", "V", "B", "N", "M"]
password_number = int(password_length)
password = []

for number in range(password_number):
    choices = random.choice(options)
    if choices == 1:
        # numbers
        choice = random.choice(numbers)
        password.append(str(choice))
    elif choices == 2:
        choice = random.choice(letters)
        password.append(str(choice))
        # letters
    elif choices == 3:
        choice = random.choice(uppercase)
        password.append(str(choice))
        # uppercase
    elif choices == 4:
        choice = random.choice(misc)
        password.append(str(choice))
        # misc
    elif choices not in options:
        print("an error was met")
    password_given = "".join(password)
print(password_given)
