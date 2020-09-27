""":arg
Any identified which start with __name cannot be access outside with instance variable.
It can be accessed if its like __name but not if its only __ tunder ( 2 underscore )
and would give AttributeError exception
"""

class A:
    def __init__(self,v):
        self.__a = v + 1
        self._b=4

    def __prn(self):
        print("hi")

a = A(0)
print(a.__a)
print(a.__prn())