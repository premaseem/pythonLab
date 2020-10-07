"""
The var of for loop is defined isolated and is not updated inside or outside the loop
"""

i = 1
for i in range(0,4):
    print(i , end = " ")
    i = i + 1
else:
    print("Python")

print(i)