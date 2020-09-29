"""
Functional programming, functions can be saved in list and retrieved later
"""

L = [lambda x: x +8  ,lambda y: y + 9,lambda z: z + 3]
for i in range(0,len(L)):
    # will print lambda
    print(L[i])

    # will invoke lambda functions
    print(L[i](i))
