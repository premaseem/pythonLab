
l = [1,2,3,4,5]

#### MAP

def sqr(x):
    return x **2

m1 = list(map(sqr, l))
print(m1)

m2 = []
for x in l:
    m2.append(x **2)
print(m2)

m3 = [ x **2 for x in l]
print(m3)

### REDUDE

import functools

r1 = functools.reduce(lambda x,y : x +y, l)

print(r1)
r2 = 1
for x in l:
    r2 *= x

print(r2)

def myreduce(func,x):
    aggr = x[0]
    for i in x[1:]:
        aggr = func(aggr,i)
    return aggr

def add(x,y):return x+y
def mul(x,y):return x+y

r3 = myreduce(add,l)
print(r3)

