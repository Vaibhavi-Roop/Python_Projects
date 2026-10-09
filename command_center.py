from abc import ABC, abstractmethod
class Smart_Device(ABC):
    def show_device(self, name):
        print("Device name:", name)
    @abstractmethod
    def turn_on(self):
        pass
class Smart_Light(Smart_Device):
    def turn_on(self):
        print("Light is on")
class Smart_Fan(Smart_Device):
    def turn_on(self):
        print("Fan is on")
class Smart_Speaker(Smart_Device):
    def turn_on(self):
        print("Speaker is on")
light = Smart_Light()
fan = Smart_Fan()
speaker = Smart_Speaker()
light.show_device("Kitchen light")
light.turn_on()
fan.show_device("Bedroom fan")
fan.turn_on()
speaker.show_device("TV speaker")
speaker.turn_on()
class Security_Camera:
    def check_status(self):
        print("Security camera is on")
class Door_Lock:
    def check_status(self):
        print("Lock is secure")
devices = [Security_Camera(), Door_Lock()]
print("")
print("Smart Device Status")
for device in devices:
    device.check_status()