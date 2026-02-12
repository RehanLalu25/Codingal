# Test dictionary
test_dict = {'Codingal': 3, 'is': 2, 'best': 2, 'for': 2, 'Coding': 1, 'BasketballPlayer': 4}

# Convert dictionary keys to lowercase
test_dict_lower = {key.lower(): value for key, value in test_dict.items()}

print("Test Dictionary:", test_dict)

# Take input and convert to lowercase
value = input("Enter the word to check its frequency: ").lower()

# Check frequency
if value in test_dict_lower:
    print("Frequency of", value, "is:", test_dict_lower[value])
else:
    print("Word not found in dictionary.")
