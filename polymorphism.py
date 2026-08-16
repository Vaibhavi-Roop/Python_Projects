from abc import ABC, abstractmethod
class Animal(ABC):
    def move(self):
        pass 
class human(Animal):
   def move(self):
       print("I can walk.")
class snake(Animal):
    def move(self):
        print("I can crawl.")
obj = human()
obj.move()
obj_2 = snake()
obj_2.move()