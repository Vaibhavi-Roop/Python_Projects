class FamilyMember:
    def __init__(self, height, eye_colour):
        self.height = height
        self.eye_colour = eye_colour
    def show_traits(self):
        print("Height:", self.height)
        print("Eye colour:", self.eye_colour)
class Kid(FamilyMember):
    def __init__(self, age, name, height, eye_colour):
        self.name = name
        self.age = age
        super().__init__(height, eye_colour)
    def show_traits(self):
        print("Name:", self.name, "Age:", self.age)
        super().show_traits()
    def hobby(self, hobby):
        print(self.name, "loves", hobby)
Child = Kid(12, "Enya", 147, "black")
Child.show_traits()
Child.hobby("Art")