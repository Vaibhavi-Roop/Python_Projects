class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed 
    def show_details(self):
        print("Brand:", self.brand)
        print("Max Speed:", self.max_speed)
class Car(Vehicle):
    def __init__(self, mileage, brand, max_speed, colour):
        self.mileage = mileage
        self.colour = colour 
        super().__init__(brand, max_speed)
    def show_details(self):
        print("Mileage:", self.mileage)
        print("Colour:", self.colour)
        super().show_details
    def fuel_type(self, fuel):
        print("Fuel:", fuel)
car = Car(438, "Subaru Forester", 136, "blue")
car.show_details()
car.fuel_type("petrol")
                                                                                                                                                                                                                                             