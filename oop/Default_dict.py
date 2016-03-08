__author__ = 'asee2278'

from collections import defaultdict
from collections import OrderedDict


o1={'a':1,'b':2}
o2={'b':1,'a':2}

print o1 ==o1
print 'Dictionaries are equal? '

d1 = OrderedDict()
d1['a'] = 'A'
d1['b'] = 'B'


d2 = OrderedDict()

d2['b'] = 'B'
d2['a'] = 'A'

print d1 == d2
