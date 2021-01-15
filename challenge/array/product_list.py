"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Implement a function, find_product(lst), which modifies a list so that each index has a product of all the numbers present in the list except the number stored at that index.
"""
input = [1,2,3,4]
expected = [24,12,8,6]

from functools import reduce

def func(l):
    # reduce to one output
    a = reduce(lambda x,y : x *y,l )
    # list
    return [ a //x  for x in l ]

def brut(l):
    a = []
    for i in range(len(l)):
        p = 1
        for j in range(len(l)):
            if j != i:
                p *= l[j]
        a.append(p)
    return a

assert expected == brut(input)
assert expected == func(input)

