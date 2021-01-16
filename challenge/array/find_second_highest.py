"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Implement a function find_second_maximum(lst) which returns the second largest element in the list.
"""

i = [9,2,3,6]
e = 6

def find_second_maximum1(lst):
    lst.sort()
    return lst[-2]



def find_second_maximum(lst):
    fh = float('-inf')
    sh = float('-inf')
    for e in lst:
        if e > fh :
            fh = e
    for e in lst:
        if e != fh and e > sh:
            sh =e
    return sh


def find_second_maximum2(lst):
    fh = float('-inf')
    sh = float('-inf')
    for e in lst:
        if e > fh :
            sh = fh
            fh = e

        elif e != fh and e > sh:
            sh = e
    return sh

    for e in lst:
        if e != fh and e > sh:
            sh =e
    return sh

assert e == find_second_maximum(i)
assert e == find_second_maximum1(i)
assert e == find_second_maximum2(i)


