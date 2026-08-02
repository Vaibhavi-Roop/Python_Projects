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
