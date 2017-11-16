nums = [-100,-20,-5,0,24,50,73,88,120]
x = int(input("Enter number:"))
found_index = -1
for index, num in enumerate(nums):
    if x == num:
        print("Found")
        # print ("Your number is",x,"in",index + 1)
        found_index= index
        break
    # if x not in nums:
    #     print ("Not found")
if found_index == -1:
    print("Not found")
else:
    print("Found:", found_index)    
