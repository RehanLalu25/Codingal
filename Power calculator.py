number = int(input("Enter the number: "))
n = int(input("Enter the number of powers required: "))

i = 1
while i <= n:
    print(number, "power", i, "=", number ** i)
    i = i + 1
