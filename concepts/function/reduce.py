"""
Reduce func
"""

__author__ = "Aseem Jain"
__profile__ = "https://www.linkedin.com/in/premaseem/"

import functools
def mul(x,y):
    print("x=",x," y=",y)
    return x*y

fact=functools.reduce(mul, range(1, 8))
print ('Factorial of 8: ', fact)