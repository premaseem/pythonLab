"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

An enumeration is a set of symbolic names (members) bound to unique, constant values.
Within an enumeration, the members can be compared by identity, and the enumeration itself can be iterated over

Enumerations are Python classes, and can have methods and special methods as usual.
 If we have this enumeration:

"""
from enum import Enum
class Mood(Enum):
    FUNKY = -1
    HAPPY = 100

    def describe(self):
       # self is the member here
       return self.name, self.value

    def __str__(self):
             return 'Mood Enum: {0}'.format(self.name)

    @classmethod
    def favorite_mood(cls):
    # cls here is the enumeration
         return cls.HAPPY

mood = ()
print(Mood.FUNKY)
print(Mood.FUNKY.name)
print(Mood.FUNKY.value)
print(Mood.FUNKY.describe())
print(Mood.HAPPY.favorite_mood())

for m in Mood:
    print(m)

print(f"get enum by name")
print(Mood["FUNKY"])
print(type(Mood["FUNKY"]))

print(f"get enum by value")
print(Mood(100))