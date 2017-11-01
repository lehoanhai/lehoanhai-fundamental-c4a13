# n = input("What's your name?")
# print("Hello", n)
# yob = int(input("what year of birth? "))
# u = 2017 - yob
# print("Oh,so u are",u)
# print("Hello World")
# print(n ,"Wanna play?")
# if u < 10:
#     print("Wait,U are baby?!?")
# elif u <18:
#     print("Strong man,arent u?")
# else:
#     print("Well,dud")
# print("Bye bye")
print("do ax^2 + bx + c = 0?")
a = int(input("what is a?"))
b = int(input("what is b?"))
c = int(input("what is c?"))
th = b*b -4*a*c
if th <0:
    print("have no solutions")
elif th==0:
    x = -b/(2*a)
    print("have 2 same solutions and it is", x)
else:
    th_root = th ** 0.5
    X1 = (-b +th_root)/(a*2)
    X2 = (-b -th_root)/(a*2)
    print("have 2 diffrent solutions and it are x1={0}, x2={1}".format(X1,X2))
