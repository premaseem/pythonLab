
import functools

l = [1,2,3,4,5,6,7,8]

sum = functools.reduce(lambda x,y : x+y , l )
print(sum)

def myreduce(func, lst):
    aggr = lst[0]
    for i in lst[1:]:
        aggr = func(aggr,i)
    return aggr

mylamda = lambda x,y : x+y
def sum(x,y):
    return x+y

sum1 = myreduce(sum,l )
print(sum1)