e = 0
from random import randrange
n = randrange(1, 101)
    # for i in range(8):
p = True
while p:
    u = int(input("Guess my number: "))
    if u > n:
        print("It is a bit large")
    elif u==n:
        print("Bingo")
        break
        # p = False
    elif u < n:
        print("It is a bit small")
