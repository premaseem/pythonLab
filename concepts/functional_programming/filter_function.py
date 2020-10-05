"""

Filter needs a filter condition which returns true when satisfied ( returning false or None is no even needed ;-)
Using filter() the Car_filter function is called and the number of times the Car_filter function called is equal to the number of elements in the list speeds.

If the function Car_filter returns a Non-empty value or Non-Zero value or boolean True value for an element from the list passed to the Car_filter function, that element will be added to the filter object.

If the function Car_filter returns an Empty value or Zero value or boolean False value or None for an element from the list passed to the Car_filter function, that element will not be added to the filter object.

Non-empty value:-  Non empty list [1,2,3], Non empty string "783" etc.

Non-Zero value:-  2, 23.365 etc.

Empty value:- empty list [], empty string "" etc.

Zero value:- 0.0, 0.
"""

def Car_filter(speed):
    if speed >100:
        return True
    else :
        return 0

speeds = [400,100,490,20,60,800,72]
obj = filter(lambda x : x > 100,speeds)
print(list(obj))