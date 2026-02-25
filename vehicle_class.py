class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage
modelx = Vehicle(240,18)
print("Model Max speed: ",modelx.max_speed)
print("Model Mileage: ", modelx.mileage)        