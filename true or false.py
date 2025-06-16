# a class that defines questions
class question:
    def __init__(self, question, answer, blurb):
        self.question = question
        self.answer = answer
        self.blurb = blurb


# all the question info
question1 = question(
    "The Amazon Rainforest produces 20% of the world's oxygen.", "False", " While often claimed, the Amazon’s net oxygen contribution is close to zero because the forest also consumes what it produces through decomposition."
)
question2 = question(
    "Mount Everest is the tallest mountain in the world above sea level.",  "True", "Everest stands at 8, 848.86 meters(29, 031.7 feet), making it the highest point on Earth above sea level."
)
question3 = question(
    "Australia is both a country and a continent.", "True", "Australia is unique in being both a country and an entire continent, with its own distinct ecosystems and geography."
)
question4 = question(
    "The Sahara Desert is the largest desert in the world.", "False", "Antarctica is actually the largest desert due to its low precipitation, making it a cold desert."
)
question5 = question(
    "Russia spans 11 time zones.", "True", "Russia is the largest country by area and stretches across 11 time zones, more than any other nation."
)
question_list = [question1, question2,
                 question3, question4, question5]


# a function that asks the question and responds
def question_interaction(question_num, score):
    print(question_num.question)
    move_on = False
    while move_on == False:
        responce = input("So do you think its True or False? ")
        if responce == ("true") or responce == ("false") or responce == ("True") or responce == ("False"):
            if responce.casefold() == question_num.answer.casefold():
                print(f"\nIndeed it was {responce}")
                score += 1
                print(f"Thats {score}/5\n")
                move_on = True
            else:
                print(
                    f"\nSorry but the answer we were looking for was {question_num.answer}")
                print(f"Thats {score}/5\n")
        else:
            print("error")
    return score


# runs; the def for each question
score = 0
for item in question_list:
    score = question_interaction(item, score)
print(f"GAME OVER\nYour Final Score = {score}/5")
