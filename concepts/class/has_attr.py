"""
Syntax : hasattr(obj, key)

Parameters :
obj : The object whose which attribute has to be checked.
key : Attribute which needs to be checked.

Returns : Returns True, if attribute is present else returns False.
"""

class A:
    A = 1

    def pnt(self):
        print("hi")

print(hasattr(A,'A'))
print(hasattr(A,'pnt'))

a = A()
print(hasattr(a,'A'))
print(hasattr(a,'pnt'))

