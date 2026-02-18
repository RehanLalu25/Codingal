print("Select what you want to do :")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice = int(input("Enter your choice"))
if choice == 1:
    rehan = int(input("Enter the first number"))
    rehan2 = int(input("Enter the second number"))
    SumofTheNumbers = rehan + rehan2
    print("The Sum of the numbers you just entered = ", SumofTheNumbers)
elif choice == 2:
    rehan3 = int(input("Enter the first number"))
    rehan4 = int(input("Enter the second number"))
    DifferenceOfTheNumbers = rehan3 - rehan4
    print("The Difference of the numbers you just entered = ", DifferenceOfTheNumbers)
elif choice == 3:
    rehan5 = int(input("Enter the first number"))
    rehan6 = int(input("Enter the second number"))
    ProductOfTheNumbers = rehan5 * rehan6
    print("The Product of the numbers you just entered = ", ProductOfTheNumbers)
elif choice == 4:
    rehan7 = int(input("Enter the first number"))
    rehan8 = int(input("Enter the second number"))
    QuotientOfTheNumbers = rehan7 / rehan8
    print("The Quotient of the numbers you just entered = ", QuotientOfTheNumbers)  
else:
    print("Enter a valid choice please!")           