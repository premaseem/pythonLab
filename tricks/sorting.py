__author__ = 'Aseem Jain'

# In place sorting in reverse order
l=[3,6,5,1,9,45]
l.sort(reverse=True)
print(l)

# output
# [45, 9, 6, 5, 3, 1]

# Sorting a custom object based on the key
class person:
    def __init__(self,name,age):
        self.name = name
        self.age=age

    def __repr__(self):
        return self.name + " : " + str(self.age)

people = [person("aseem",36),person("zank",32),person("boo",22)]
print("original sequence", people)

# sort using key by lambda for attribute
people.sort(key=lambda x:x.name)
print("sorted by Name",people)

# sort using key by lambda for attribute
people.sort(key=lambda x:x.age)
print("sorted by Age",people)

# Reverse sort using key by lambda for attribute
people.sort(key=lambda x:x.age,reverse=True)
print("sorted by age in reverse",people)