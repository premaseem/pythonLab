__author__ = 'asee2278'



seq1 = range(1,45,3)
seq2 = range(10,4500,50)
seq3 = range(1,45,3)
seq4 = range(1,45,3)

def inr2usd(amt):
    return amt / 65.0


result1 = map(lambda x : x/65.0 ,range(10))
result2 = reduce(lambda x,y:x+y, range(10))
result3 =filter(lambda  x : x%2 ==0, range(10))

l1 = [1,2,3,4,5]
l2=[2,4,6,8]
l3=[3,6,9,12]
d1={"a":1,"b":2,"c":3}
d2={"d":11,"e":12,"f":13}


val = zip(l1,l2,l3,d1,d2.iteritems())
print type(val)
print val
# print val
# print reduceResult