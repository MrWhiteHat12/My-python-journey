print("imput only numbers")
total = input("how much was the bill total: $")
percetage = input(
    "what percetage would you like to tip (5, 10, 12, 15, custom): ")
number_of_people = input("how people are you splitting the bill between: ")
total_per_person = ("error")
use_proper = True

try:
    total = float(total)
    percetage = float(percetage)
    number_of_people = float(number_of_people)
except ValueError:
    use_proper = False

percetage = int(percetage)/100

percetage = float(total)*percetage

total = float(total)+float(percetage)

total_per_person = total/int(number_of_people)

if use_proper == True:
    print(f"${total_per_person}")
else:
    print("error imput only numbers")
