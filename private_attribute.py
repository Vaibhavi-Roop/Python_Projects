class Account:
    def __init__(self, owner,  pin):
        self.owner = owner
        self.__pin = pin        
    def show_pin_status(self):
        print("Owner:", self.owner)
    def set_pin(self, new_pin):
        if len(new_pin) == 4 and new_pin.isdigit():
            self.__pin = new_pin
            print("PIN updated")
        else:
            print("Invalid PIN")
    def check_pin(self, entered_pin):
        if entered_pin == self.__pin:
            print("Acess granted")
        else:
            print("Acess denied")
    def __str__(self):
        return "Account holder" + self.owner
account  =Account("Ava", "3647")
print(account)
account.show_pin_status()
account.__pin = "2957"
print("Output of pin changed from the outside the class")
account.check_pin("2957")
account.check_pin("3647")
account.set_pin("1582")
account.check_pin("1582")