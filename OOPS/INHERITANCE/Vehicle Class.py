class Vehicle:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def displayinfo(self):
        print("model = " + self.model)
        print("brand = " + self.brand)
class Car(Vehicle):
    pass
class Bike(Vehicle):
    pass

b1 = Bike("hero","splender")
c1 = Car("Toyota","Prius")
print("car details")
c1.displayinfo()
print("bike details")
b1.displayinfo()