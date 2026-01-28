age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    if age % 2 == 0:
        print("The age entered is an even number.")
    else:
        print("The age entered is an odd number.")
else:
    print("ValueError: Please enter a valid integer age.")
