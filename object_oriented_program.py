class student:
    grade = 7
    print("Hi I'm in grade", grade)
object = student()

class vehicle:
    def __init__(self, maximum_speed, milage):
        self.maximum_speed = maximum_speed
        self.milage = milage
car = vehicle(347, 18)
bike = vehicle(89, 12)
print("The maximum speed of the car is", car.maximum_speed)
print("The milage of the car is", car.milage)
print("The maximum speed of the bike is", bike.maximum_speed)
print("The milage of the bike is", bike.milage)

class parrot:
    species = 'parrot'
    def __init__(self, name, age):
        self.name = name
        self.age = age
Rosetta = parrot("Rosetta", 6)
Avery = parrot("Avery", 12)
print("The first parrot is called", Rosetta.name)
print("The second parrot is called", Avery.name)
print("Rosetta is a", Rosetta.species)
print("Avery is a ", Avery.species)
print("Rosetta is", Rosetta.age, "years old")
print("Avery is", Avery.age, "years old")