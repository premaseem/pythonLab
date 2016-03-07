__author__ = 'asee2278'

#1 generating classic febonacchi series

fs=[0,1]
n=[]
n1=0
n2=0
lst = range(0,15)
for i,x in enumerate(lst):
    if i<2 : continue
    print fs[i-2] ,fs[i-1],
    num = fs[i-2] + fs[i-1]
    print num
    fs.append(num)

print fs

#2 generating febonacchi series
a=1
b=1

for x in range(10):
    t=a
    a=b
    b=b+t
    print b

print "################"
#3 generating febonacchi series
def genfibon(n):
    '''
    Generate a fibonnaci sequence up to n
    '''
    a = 1
    b = 1
    for i in range(n):
        yield a
        a,b = b,a+b

lst = genfibon(1000)

type(lst)
for num in lst:
    print num