class My_class:
    __privateVar = 27

    def __privateMethod(self):
        print("I am inside private method")
    def hello(self):
        print("I am inside class My_class")

f = My_class()
f.hello
f.__privateMethod


class Computer:
    __maxprice = 3265
    def sellingprice(self,price):
        print("selling price", self.__maxprice )
    def setmaxprice(self, price):
        self.__maxprice = price 
d = Computer()
d.sellingprice(694)
d.__maxprice = 16216289
d.sellingprice()