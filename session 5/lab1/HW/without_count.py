nums = [1,6,8,1,2,1,5,6]
num = int(input("Your Number: "))
c = []
for i in range (len(nums)):
    if nums[i] == num:
        c.append(nums[i])
print(num, "appear",len(c),"times in my list")
