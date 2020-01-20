#!usr/bin/python3

# Generator-Function : A generator-function is defined like a normal function, but whenever it needs to generate a value, it does so with the yield keyword rather than return.
# If the body of a def contains yield, the function automatically becomes a generator function.


######################################
# Your own range generator using yield


# A generator function that yields 1 for first time,
# 2 second time and 3 third time
def simpleGeneratorFun():
    yield 1
    yield 2
    yield "3"

o = simpleGeneratorFun()
print(type(o))
# for n in o:
#     print(n)

# Iterating over the generator object using next
print(next(o)); # In Python 3, __next__()
print(next(o));
print(next(o));
print(next(o));

######################################


def my_range(start, end, step):
    while start <= end:
        yield start
        start += step

seq = my_range(1, 10, 0.5)
print("aseem")
for x in seq:
    print(x, end=" ")

######################################

import sys
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration as e:
      sys.exit()


