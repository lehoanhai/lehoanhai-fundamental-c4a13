# menu = ['chan ga nuong', 'ga sao', 'ga chay']
# print (*menu,sep=', ')
# print(" * "*10)
# menu.append('ga rau')
# print (*menu,sep=', ')
print ("Hi there, Here some of your favorite")
like = ['game','anime','design']
print (*like,sep=', ')
print (' * '*10)
n = input("what do u want to add? ")
like.insert(0,n)
print (*like,sep=", ")
