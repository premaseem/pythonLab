"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/
O(Log(n))
"""

n = 10


def logn():
    total_operation = 0
    t = 1
    while t < n:
        total_operation += 1
        t = t * 2
    return total_operation

def On():
    total_operation = 0
    t = 1
    while t < n:
        total_operation += 1
        t = t +1
    return total_operation

def Nlogn():
    total_operation = 0
    t = 1
    for i in range(n):
        t = 1
        while t < n:
            total_operation += 1
            t = t * 2
    return total_operation

def nSquare():
    total_operation = 0
    ot = 1
    while ot < n:
        ot += 1
        t = 1
        while t < n:
            total_operation += 1
            t = t + 1

    return total_operation

def nexpn(p,total_operation):
    if p == 10:
        return 1
    for i in range(10):
        total_operation += 1

    return total_operation + nexpn(p+1,total_operation)


print("total operation would be log n: ",logn())
print("total operation would be N: ",On())
print("total operation would be N log n: ",Nlogn())
print("total operation would be N Square: ",nSquare())
print("total operation would be N exp n: ",nexpn(1,2))



