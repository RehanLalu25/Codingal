class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity

    def fare(self):
       return self.capacity * 100


class Bus(Vehicle):
    def fare(self):
        total_fare = super().fare()
        maintenance = total_fare * 0.10
        return total_fare + maintenance


# seating capacity of bus = 50
bus = Bus(50)

print("Total Bus Fare:", bus.fare())