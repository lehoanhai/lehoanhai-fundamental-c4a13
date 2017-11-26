from random import randint,choice
from calculator import eval
# nums=range()
# kq = ['1','2','3','4','5','6','7','8','9']
# x=nums[range(0,10)]
# y=nums[range(0.10)]
# n=randint(0,11)
x=randint(0,10)
y=randint(0,10)
o = choice(['+','-','*','/'])
error = randint(-1,1)

tkq = calculator.eval(x,y,o)
kq = tkq + error
print('{0} {3} {1} = {2}'.format(x,y,kq,o))
# choice = input('T/F?')
# if choice == 'T':
#     if error==0:
#         print('yay')
#     else :
#         print('wrong')
# else:
#     if error != 0:
#         print('wrong')
#     else :
#         print('yay')





# if n =< 5:
#     kq=x+y
#     print (x,'+',y,'=',kq)
#     ans = input('T/F?')
#     if ans == T:
#         print ('Yay')
#     else:
#         print ('Oh no')
# else n<10:
