class Reverse:
    def __init__(self, s=""):
        self.s = s

    def reverse_string(self):
        return self.s[::-1]


# take input from the user
word = input("Enter a word: ")

# create object with user input
obj = Reverse(word)

# print reversed string
print("Reversed string:", obj.reverse_string())