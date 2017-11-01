from turtle import *
speed(-1)
shape ("turtle")
for i in range(1000):
    forward(i+1)
    for u in range(2):
        left(60)
        circle(50)
mainloop()
