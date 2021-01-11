"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Find Two Pairs in List such that a+b = c+d
Input
my_list = [3, 4, 7, 1, 12, 9]

Output
[[4,12],[7,9]]
"""
my_list = [3, 4, 7, 1, 12, 9]
ans = []
m = {}
def fn():
    for i, e in enumerate(my_list):
        for j in range(i+1, len(my_list)):
            k = e + my_list[j]
            v = [e, my_list[j]]
            if k not in m:
                m[k] = []
            m[k].append(v)
            if len(m[k]) > 1:
                return m[k]
    # return m
print(fn())




