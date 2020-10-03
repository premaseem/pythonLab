"""
The closure contains enclosed scope of function.
with the init variable
"""

def make_multiplier_of(n):
    def multiplier(m):

        return n * m
    return multiplier

table5 = make_multiplier_of(5)
table2 = make_multiplier_of(2)
print(table5(10))
print(table2(10))