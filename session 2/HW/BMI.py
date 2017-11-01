print ("This is BMI text")
height = int(input("Enter your height here:(cm) "))
mass = int(input("Enter your weight here:(kg) "))
BMI = mass*10000 /(height * height)
if BMI < 16:
    print("You are severely underweight")
elif BMI < 18.5:
    print("You are underweight")
elif BMI < 25:
    print("You are normal")
elif BMI < 30:
    print("You are overweight")
else:
    print("You are obese")
