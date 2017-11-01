
u = input("Your choise:bua,keo,la? ")
from random import randrange
n = randrange(1,100)
# print ("Hello there Im Moody")
# if n < 30:
#     print("I kind of sad")
# elif n < 70:
#     print("I am fine")
# else:
#     print("I feel sooo great")
if n < 30:
    if u == "bua":
        print("Game choise: keo")
        print("You win")
    elif u == "keo":
        print("Game choise: keo")
        print("It's a draw")
    else:
        print("Game choise: keo")
        print("You lose")
elif n < 60:
    if u == "bua":
        print("Game choise: bua")
        print("It's a draw")
    elif u == "keo":
        print("Game choise: bua")
        print("You lose")
    else:
        print("Game choise: bua")
        print("You win")
else:
    if u == "bua":
        print("Game choise: la")
        print("You lose")
    elif u == "keo":
        print("Game choise: la")
        print("You win")
    else:
        print("Game choise: la")
        print("It's a draw")
