"""
when you print and object, the __str__ actually calls the __repr__,
so make your object show details you can override __repr__

The official Python documentation says __repr__() is used to compute the “official” string representation of an object.
The repr() built-in function uses __repr__() to display the object. __repr__()  returns a printable representation of the object, one of the ways possible to create this object.  __repr__() is more useful for developers while __str__() is for end users.

"""

class Point:

    def __init__(self, x, y):

        self.x, self.y = x, y
        map()

    def __repr__(self):
        return 'Point(x=%s, y=%s)' % (self.x, self.y)

p = Point(3, 4)

print (p)
# without __repr__()implemented
# <__main__.Point object at 0x11036e5c0>

# with __repr__() implemented
# Point(x=3, y=4)



