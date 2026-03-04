import random

print("Welcome to the Random Number Game!")

# Generate a random number between 1 and 10
number = random.randint(1, 10)

# Ask the user to guess
guess = int(input("Guess a number between 1 and 10: "))

# Check the guess
if guess == number:
    print("🎉 Correct! You guessed it!")
else:
    print("❌ Wrong! The correct number was:", number)

print("Thanks for playing!")