print("Here your favorite:")
menu = ['game','anime','design','f']
print(*menu,sep=', ')
print('*x'*50)
d = input("what thing u want to remove? ")
if d in menu:
    menu.remove(d)
    print(*menu,sep=', ')
else:
    print(d ,'dont in the list')
