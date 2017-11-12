menu = ['gu','ge','xi']
print ("This is wreir")
print(*menu,sep=', ')
n = int(input("what thing u want to update? "))
o = input("change to? ")
menu[n] = o
print(*menu,sep=', ')
