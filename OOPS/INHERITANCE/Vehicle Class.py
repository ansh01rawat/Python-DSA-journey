class Vehicle: #parent  
    def __init__(self,brand,model):    #constructor
        self.brand = brand    #instance attribute
        self.model = model    #instance attribute
    def displayinfo(self):       #instance method
        print("model = " + self.model)
        print("brand = " + self.brand)
class Car(Vehicle):     #child
    pass
class Bike(Vehicle):    #child
    pass
# execution
b1 = Bike("hero","splender")
c1 = Car("Toyota","Prius")
print("car details")
c1.displayinfo()
print("bike details")
b1.displayinfo()
