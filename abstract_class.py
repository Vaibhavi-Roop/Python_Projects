from abc import ABC, abstractmethod
class absclass(ABC):
    def print(self,x):
        print("Passed value", x)
    @abstractmethod
    def task(self):
        print("We are inside absclass.")
class test_class(absclass):
    def task(self):
        print("We are inside def task")

obj = test_class()
obj.task()
obj.print(100)
