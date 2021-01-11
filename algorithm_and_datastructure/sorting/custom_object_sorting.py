"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Title: Sort the class or custom object and not regular int / string using in build sort funcitons
Sort custom object can be done in 2 ways
1. Static way : class implementing < less then __lt__(self,other)
2. Dynamic way is by providing lambda func with key.
"""
class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + str(self.age)

    def __lt__(self, other):
        return self.age < other.age

# Sorting String
ls = ["zeema", "aseemjain", "see",str(3),str(13),"$$"]
ls.sort()
print(ls)
#output: ['$$', '3', 'aseemjain', 'see', 'zeema']

# Reverse soring
ls.sort(reverse=True)
print(ls)
# output: ['zeema', 'see', 'aseemjain', '3', '$$']

# sorting Custom object
users = [User("aseem",16),User("aseemprem",56),User("premaseem",23),User("zseem",36),User("nseem",106) ]
users.sort(key = lambda x: x.name)
users.sort()
print(users)
# output : [aseem16, aseemprem56, nseem106, premaseem23, zseem36]

# create new sorted list
newlist = sorted(users, key=lambda x: x.age, reverse=True)
print(newlist)
# output: [nseem106, aseemprem56, zseem36, premaseem23, aseem16]