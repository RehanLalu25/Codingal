class BMW:
    def fuel_type(self):
        print("BMW uses Petrol/Diesel")

    def max_speed(self):
        print("BMW max speed is 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("Ferrari uses Petrol")

    def max_speed(self):
        print("Ferrari max speed is 340 km/h")


for car in (BMW(), Ferrari()):
    car.fuel_type()
    car.max_speed()