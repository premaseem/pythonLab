""":arg
Python providers variable assignment at class level, apart from object level.
class var can be accessed by all objects.

Class or static variables are shared by all objects.
Instance or non-static variables are different for different objects (every object has a copy of it).

"""

class A:
    X = 0
    def __init__(self,v = 0):
        self.Y = v
        A.X += v

a = A()
b = A(1)
c = A(2)
print(c.X)
