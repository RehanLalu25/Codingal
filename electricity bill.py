unit = int(input("Please enter the number of units you consumed"))
if unit<50:
    amount = unit*2.6
    Tax = 25
elif unit<=100:
    amount = 130 + ((unit-50)*3.25)
    Tax = 35
elif unit <= 200:
    amount = 130 + 162.50((unit - 100)*5.26)
    Tax = 45
else:
    amount = 130 + 162.50 + 5.26 + ((unit - 200)*8.54) 
    Tax = 75
Total = amount + Tax
print("Electricity bill is ",Total)               