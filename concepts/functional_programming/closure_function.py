"""
The closure contains enclosed scope of function.
with the init variable,

"""
class Multiplier:
    def __init__(self,n):
        self.n = n

    def multiply(self, m):
        return self.n * m


def make_multiplier_of(n):
    def multiply(m):

        return n * m
    return multiply

table5 = make_multiplier_of(5)
table2 = make_multiplier_of(2)
print(table5(10))
print(table2(10))

obj5 = Multiplier(5)
obj2 = Multiplier(2)
print(obj5.multiply(10))
print(obj5.multiply(7))