__author__ = 'asee2278'


print bin(1024)
print hex(1024)
print round(5.23222,2)
s = 'hello how are you Mary, are you feeling okay?'
print s.islower()
print "value " + str(s.find('w'))

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}
print set1.symmetric_difference(set2)

s = {1,3,5,7}
s.discard(13)
s.add(4)

s1 = {3,4,5,6}
print s.update(s1)

d = {k:x**2 for k,x in zip(['a','b','c'],range(3))}
print d.viewvalues()

dict = {x:x**2  for x in range(5)}


{0: 0, 1: 1, 2: 8, 3: 27, 4: 64}
