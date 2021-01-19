"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Big O time complexity: O(nlog_3(n))O(nlog3(n))

"""

n = 100  # can be anything, this is just an example
sum = 0
pie = 3.14
for var in range(1, n, 3):
    j = 1
    print(pie)
    while j < n:
        sum += 1
        j *= 2
print(sum)  # O(1)


