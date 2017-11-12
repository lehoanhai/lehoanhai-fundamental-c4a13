from random import randint
word = ["gamer","random","evolution"]
hman = [
    """
    ______
    |     |
    |     0
    |
    |
    |
   _|_
    """,
    """
    ______
    |     |
    |     0
    |    _|
    |
    |
   _|_
    """,
    """
    ______
    |     |
    |     0
    |    _|_
    |
    |
   _|_
    """,
    """
    ______
    |     |
    |     0
    |    _|_
    |     |
    |    /
   _|_
    """,
    """
    ______
    |     |
    |     0
    |    _|_
    |     |
    |    /.\\
   _|_
    """
]
keyword = word[randint(0, 2)]
l = list(keyword)
list_ = []
for i in range(len(keyword) ):
    list_.append('_')
print(*list_, sep='  ')
#Correct??
sumkey = 0
hman_ = 0
for i in range(len(list_)):
    key = input("Chu cai: ")
    for j in range (len(l)):
        if key == l[j]:
            list_[j] = key
            sumkey = sumkey + 1
    if key not in l:
        hman_ = hman_ + 1
        print(5 - hman_, "Turn left")
        print(man[hman_])
        if hman_ == 4:
            print("You lose!!")
            exit
    print(*list_, sep='  ')
    if sumkey == len(list_):
        print("You win!")
        break
