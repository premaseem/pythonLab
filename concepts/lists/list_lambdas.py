"""
Functional programming, functions can be saved in list and retrieved later
"""

L = [lambda x: x +8  ,lambda y: y + 9,lambda z: z + 3]
for i in range(0,len(L)):
    # will print lambda
    print(L[i])

    # will invoke lambda functions
    print(L[i](i))

""" 
adding lambda in list comprehension as one line function. 
"""

l = [1,2,3,4]
def convert_to_str(x):
    return x

# calling external fun on each element
l = [convert_to_str(x) for x in l]

# calling lambda fun on each element
l = [(lambda x:str(x*x))(x) for x in l]
print(l)
