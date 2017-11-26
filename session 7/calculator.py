def eval(x,y,o):
    if o == '+':
        kq = x + y
    elif o == '-':
        kq = x - y
    elif o == '*':
        kq = x * y
    elif o == '/':
        if y !=0:
            kq = x / y
        else:
            kq ='Nan'
    return kq
# x=10
# y=5
# o='+'
# r = eval(x,y,o)
# print (r)
#


# x = int(input("x ="))
# o = input("Operation(+,-,*,/):")
# y = int(input("y ="))
# if o in ['+','-','*','/']:
#     r = eval()
#
#     print('*'*20)
#     print(x,o,y,'=',r)
# else:
#     print ('Error')
