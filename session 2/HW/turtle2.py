from turtle import *
shape("arrow")
speed(-1)
# color("blue")
# for i in range(3):
#     forward(100)
#     left(120)
# color("red")
# for i in range(4):
#     forward(100)
#     left(90)
# color("blue")
# for i in range(5):
#     forward(100)
#     left(72)
# color("red")
# for i in range(6):
#     forward(100)
#     left(60)
for n in range(3, 100):
    for _ in range(n):
        forward(100)
        left(360 / n)
mainloop()
