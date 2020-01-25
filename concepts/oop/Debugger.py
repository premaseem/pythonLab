__author__ = 'asee2278'
import pdb
import timeit


# For loop
time_to_execute = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print time_to_execute
# List comprehension

time_to_execute = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print time_to_execute
# Map()

time_to_execute = timeit.timeit('"-".join(map(str, range(100)))', number=10000)
print time_to_execute

########################

x = [1,3,4]
y = 2
z = 3

result = y + z
print result

# Set a trace using Python Debugger

pdb.set_trace()
result2 = y+x
print result2

