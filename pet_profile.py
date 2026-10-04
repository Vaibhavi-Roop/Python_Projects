class Pet:
    print("Hi! This is a Pet Profile class!")
pet_object = Pet()

class Pet_Profile:
    category = "pet"
    def __init__(self, name, species, age, breed):
        self.name = name
        self.species = species 
        self.age = age 
        self.breed = breed 
pet_1 = Pet_Profile("Waffle", "Dog", 8, "Goldendoodle")
pet_2 = Pet_Profile("Rosabelle", "Cat", 1, "Maine Coon")
print("{} is a {} and he is {} months old.". format(pet_1.name, pet_1.breed, pet_1.age))
print("{} is a {} and she is {} year old.".format(pet_2.name, pet_2.breed, pet_2.age))