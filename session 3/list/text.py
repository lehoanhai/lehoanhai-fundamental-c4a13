from random import choice
w = "hohlo"
charater = list(w)

for i in range(5):
    c = choice(charater)
    print(c,end=' ')
    charater.remove(c)
