B = int(input("How many B bacterias are there? "))
time = int(input("How much time in minutes will we wait? "))
if time % 2 == 0 and time != 0:
    for i in range(0,time,2):
        B = B * 2
    print("After {0} minutes, we would have {1} bacterias".format(time,B))
elif time  == 0 or time ==1:
        print("It still",B)
else:
    even_time = time - 1
    for i in range(0,even_time,2):
        B = B * 2
    print("After {0} minutes, we would have {1} bacterias".format(time,B))
