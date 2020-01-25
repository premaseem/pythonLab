__author__ = 'asee2278'
#
from collections import Counter
#
# l=[1,2,3,4,5,1,2,3,4,5,9,8,7,6,4,44,5]
#
# print Counter(l)

s = 'How many times does each word show up in this sentence word times each each word'
words = s.split()
c= Counter(words)
print c
print c.most_common(2)

print sum(c.values())
print list(c)

for k,v in c.items() :
    print k,v