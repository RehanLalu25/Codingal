try:
    number = int(input("Enter a nummber !"))
    print("The number entered is ",number)
except ValueError as ex:
    print("Execption: ",ex)    