__author__ = 'asee2278'

from collections import namedtuple

dog = namedtuple('Dog',"name color size")
kallu = dog(name="kallu", color="black", size="small")
print kallu.name
for x in kallu :
    print x


Container = namedtuple('Container', ['name', 'date', 'foo', 'bar'])
mycontainer = Container('name', 'date', 'foo', 'bar')
print mycontainer
