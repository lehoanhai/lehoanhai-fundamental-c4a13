prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}
stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
for i in prices:
    print("{0}: {1}".format(i, prices[i]))
    print("{0}: {1} \n".format(i, stock[i]))

tl = 0

for i in prices:
    multiply = stock[i] * prices[i]
    print("if you sell all {0}, you will get {1}".format(i, multiply))
    tl += multiply

print("Total get is :", tl)
