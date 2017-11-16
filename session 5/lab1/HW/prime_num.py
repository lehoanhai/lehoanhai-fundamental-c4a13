num = int(input("Enter Your Number: "))
if num == 2:
    print(num,"is prime")
elif num > 2:
    if num % 2 == 0:
        print(num,"is not a prime number")
    else:
        print(num,"is a prime")
else:
    print(num,"is not a prime")
