# Parent class
class Bird:

    # Constructor
    def __init__(self):
        print("Bird is ready")

    # Method
    def whoisThis(self):
        print("Bird")

    # Method
    def swim(self):
        print("Swim faster")


# Child class
class Penguin(Bird):

    # Constructor
    def __init__(self):
        # Call parent constructor
        super().__init__()
        print("Penguin is ready")

    # Overriding method
    def whoisThis(self):
        print("Penguin")

    # New method
    def run(self):
        print("Run faster")


# Creating object
peggy = Penguin()

# Calling methods
peggy.whoisThis()
peggy.swim()
peggy.run()