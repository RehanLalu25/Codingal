print("SELECT YOUR RIDE:")
print("1. bike")
print("2. car")
CHOICE = int(input("ENTER YOUR CHOICE! "))
if CHOICE == 1:
    print("WHAT TYPE OF BIKE???")
    print("1. SCOOTY")
    print("2. SCOOTER")
    CHOICE2 = int(input("ENTER YOUR CHOICE! "))
    if CHOICE2 == 1:
        print("YOU HAVE SELECTED SCOOTY!!!")
    else:
        print("YOU HAVE SELECTED SCOOTER")
elif CHOICE == 2:
    print("WHICH TYPE OF CAR???")
    print("1. SUV")
    print("2. SADAN")
    CHOICE2 = int(input("ENTER YOUR CHOICE! "))
    if CHOICE2 == 1:
        print("YOU HAVE SELECTED SUV!!!")
    else:
        print("YOU HAVE SELECTED SADAN")
else:
    print("wrong choice")                           