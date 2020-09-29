"""
Define if objects are equal
"""

class Car:
    def __init__(self,x,y):
        self.name = x
        self.price = y

    def __eq__(self,other):
        return self.name == other.name and self.price == other.price


obj1 = Car('Audi',2000)
obj2 = Car('Audi',2000)

# value equality
print(obj1 == obj2)

# object reference equality
print(obj1 is obj2)