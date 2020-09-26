
"""
Break, actually breaks only the current loop, if that loop is nested, it will still continue
the outer loop as usual.
Break can only be used inside loops - for / while
"""

for x in range(5):
    print("x=",x)

    for y in range(1,5):
        print(f"   {x}  y=",y)
        if y%2==0:break
