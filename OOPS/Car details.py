class Car:
    def __init__ (self,brand,model,speed):
        self.brand = brand
        self.model = model
        self.speed = speed
    def display(self):
        print("brand:",self.brand)
        print("model:",self.model)
        print("speed:",self.speed)
car1 = Car("Audi","Q8","240 mph")
car2 = Car("BMW","m4","320 mph")
car1.display()
car2.display()