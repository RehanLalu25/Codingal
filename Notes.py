amount = int(input("enter the amount"))
note100 = amount//100
note50 = (amount%100)//50
note10 = ((amount%100)%50)//10
print("notes of 100 rupees:",note100)
print("notes of 50 rupees:",note50)
print("notes of 10 rupees:",note10)