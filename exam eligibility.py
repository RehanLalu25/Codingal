medical_cause = input("Did you have a medical cause? Y or N?")
attend = int(input("Enter the attendence of the student"))
if medical_cause== "Y":
    print("Your are allowed")
else:
    if attend>= 75:
        print("Your allowed")
    else:
        print("Not allowed")
        
            