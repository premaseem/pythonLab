
"""
continue, actually jumps up to the top of only the current loop, and does not affect any outer loop
continue can only be used inside loops - for / while
"""

print("print only odd number with continue")
for x in range(5):
    print("x=",x)

    for y in range(1,5):
        if y%2==0:continue
        print(f"   {x}  y=",y)

