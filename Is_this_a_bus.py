class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class BUS(Vehicle):
    pass
School_bus = BUS("School Volvo", 180,12)
print("vehicle Name:", School_bus.name, "Speed", School_bus.max_speed,"Mileage:",School_bus.mileage)
