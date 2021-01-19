"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/
O(n2)
"""

n = 10  # n can be anything, this is just an example
sum = 0
pie = 3.14

for var in range(1, n, 3):
    print(pie)
    for j in range(1, n, 2):
        sum += 1
        print(sum)
