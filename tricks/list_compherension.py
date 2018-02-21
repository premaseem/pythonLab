__author__ = 'Aseem'

"""
vals = [expression for value in collection if condition]

# This is equivalent to:

vals = []
for value in collection:
    if condition:
        vals.append(expression)
"""

# conventional way
vals = []
for x in range(10):
    if not x % 2:
        vals.append(x * x )

print(vals)

# list comprehensions way
even_squares = [x * x for x in range(10) if not x % 2]
print(even_squares)


""" Sample out put """

# >>> even_squares = [x * x for x in range(10) if not x % 2]
# >>> even_squares
# [0, 4, 16, 36, 64]