__author__ = 'asee2278'


from collections import namedtuple

Car = namedtuple("car", "color miledge")
# Using namedtuple is way shorter than
# defining a class manually:


# Our new "Car" class works as expected:
my_car = Car('red',122)
#my_car.color


# We get a nice string repr for free:
#>>> my_car
#Car(color='red' , mileage=3812.4)

# Like tuples, namedtuples are immutable:
#>>> my_car.color = 'blue'
#AttributeError: "can't set attribute"