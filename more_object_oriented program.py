class IOString:
    def __init__(self):
        self.string_1 = ""
    def get_string(self):
        self.string_1 = input("Enter a sentence:")
    def show_string(self):
        print("The result is", self.string_1.upper())
string_1 = IOString()
string_1.get_string()
string_1.show_string()

class employee:
    def __init__(self):
        print("Employee created")

    def __del__(self):
        print("Destructor called")
def create_obj(self):
    print("Creating object")
    obj = employee()
    return obj
print("Calling create object function")
obj = create_obj
print("Program end")
