__author__ = 'asee2278'
import random

#1 Create a generator that generates the squares of numbers up to some number N.

def gensquares(top):
    for num in range(top):
        yield num **2

for x in gensquares(10):
    print x


#2 Create a generator that yields "n" random numbers between a low and high number (that are inputs). Note: Use the random library. For example:

def rand_num(low,high,n):
    for num in range(n):
        yield random.randint(low,high)


for num in rand_num(1,10,12):
    print num



#3 Use the iter() function to convert the string below
s = 'hello'
s = iter(s)
print s.next()

import itertools
horses = [1, 2, 3, 4]
#print(list(itertools.permutations(horses)))

def yeildThree(num):
    yield num +1
    yield num +2
    yield num +3

x = yeildThree(5)
# print x.next()
# print x.next()
# #print x.next()
# print x.next()