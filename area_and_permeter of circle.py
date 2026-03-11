import math

class Circle:
    # constructor
    def __init__(self, radius):
        self.radius = radius

    # function to calculate area
    def area(self):
        return math.pi * self.radius ** 2

    # function to calculate perimeter (circumference)
    def perimeter(self):
        return 2 * math.pi * self.radius


# take radius input from user
r = float(input("Enter the radius of the circle: "))

# create object
c = Circle(r)

# display results
print("Area of the circle:", c.area())
print("Perimeter of the circle:", c.perimeter())