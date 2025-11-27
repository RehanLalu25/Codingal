height = float(input("Enter your height:"))
weight = float(input("Enter your weight:"))
BMI = weight/(height/100)**2
print("Your BMI is:",BMI)
if BMI<=18.4:
    print("your underweight")
elif BMI <= 24.9:
    print("you are healthy")
elif BMI <=29.9:
    print("you are overweight")        
elif BMI <= 34.9:
    print("your are severly overweight")
elif BMI <= 39.9:
    print("you are obese")
else:
    print("you are severly obese")        