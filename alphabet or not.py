character = input("Enter a character: ")

if len(character) == 1:  # Ensure only one character is entered
    if character.isalpha():
        print("YES ITS AN AN ALPHABET.")
    else:
        print("ITS NOT AN ALPHABET.")
else:
    print("Please enter only ONE character.")
