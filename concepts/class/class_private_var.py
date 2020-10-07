"""
Any var with __var cannot be accessed outside the scope of class.
We did var shadowing, the var from super class is called.
"""

class Bike:
    def __init__(self):
        self.__Company_name = "BMW"
        self.price = 2000
    def details(self):
        print('Name : ',self.__Company_name,'Price : ',self.price)

class Car(Bike):
    def __init__(self):
        super().__init__()
        self.__Company_name = "Audi"
        self.price = 4000



obj = Car()
obj.details()