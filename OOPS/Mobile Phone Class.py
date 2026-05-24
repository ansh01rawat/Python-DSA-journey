class Mobile_Phone:
    def __init__(self, model,brand,price):
        self.model = model
        self.brand = brand
        self.price = price
    def display_details(self):
        print(self.model)
        print(self.brand)
        print(self.price)

    def update_price(self):
        self.price = self.price * 1.2
        print("latest price:",self.price)


mob1 = Mobile_Phone("17 pro","apple", 141999)
mob1.display_details()
mob1.update_price()

mob2 = Mobile_Phone("17 pro max","apple", 151999)
mob2.display_details()
mob2.update_price()