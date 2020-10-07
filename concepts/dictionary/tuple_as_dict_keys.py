"""
dict keys could be string or even tuple but not list
since tuple is immutable and hashable
Plz note list, set and dict cannot be used as keys in dict
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


details = dict()
# details = {['Audi','BMW'] : ['Price : 2000' , 'Year : 1958']}
# details[{'Audi','BMW'}] = {'Price : 2000' , 'Year : 1958'}
# details[{'Audi':1,'BMW':2}] = {'Price' : 2000 , 'Year' : 1958}