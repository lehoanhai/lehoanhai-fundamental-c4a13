num = [-100,-20,0,11,20,40]
start = 0
stop = len(num)
x = int(input("enter nums:"))
found_index = -1
while start != stop:s
        found_index = mid
        break
    elif num[mid] < x:
        mid = (stop +start+1)//2
        start = mid
    else:
        mid = (stop +start)//2
        stop = mid
if found_index == -1:
    print ("Not found")
else:
    print ("found at",found_index)
    print
