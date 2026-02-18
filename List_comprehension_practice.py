# Take input from user
n = int(input("Enter a number: "))

# List of all odd numbers under n
odd_numbers = [i for i in range(n) if i % 2 != 0]

# Another list of odd numbers (example: squares of odd numbers)
odd_squares = [i**2 for i in range(n) if i % 2 != 0]

print("Odd numbers:", odd_numbers)
print("Squares of odd numbers:", odd_squares)

