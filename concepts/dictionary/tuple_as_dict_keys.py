"""
dict keys could be string or even tuple but not list
since tuple is immutable and hashable
"""

result = dict()
result[(1,2,3)] = 34
result[(2,3,1)] = 40
result[(3,1,2)] = 13

print(result)

l = [(1,2,3),(2,3,1),(3,1,2)]
summ = 0
for i in l:
    summ = summ + result[i]

print(summ)