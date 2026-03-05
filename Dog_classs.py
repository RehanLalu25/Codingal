class Dog:
    # Class variable
    animal = "Dog"

    # Constructor
    def __init__(self, breed, colour):
        self.breed = breed
        self.colour = colour

    # Method to display details
    def display_details(self):
        print("Animal:", Dog.animal)
        print("Breed:", self.breed)
        print("Colour:", self.colour)
        print("---------------------")


# Creating two objects
dog1 = Dog("Labrador", "Black")
dog2 = Dog("German Shepherd", "Brown")

# Displaying details
dog1.display_details()
dog2.display_details()