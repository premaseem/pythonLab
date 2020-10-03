seq = [1,2,3,4,5,6,7,8,10]

# evens = list(filter(lambda x : x %2 == 0, seq ))
# odds = list(filter(lambda x : x %2 != 0, seq ))
# print(evens)
# print(odds)

def is_even(x):
    if x % 2 == 0:
        return True
    return False

evens = list(filter(is_even, seq ))
# odds = list(filter(lambda x : x %2 != 0, seq ))
print(evens)
# print(odds)

# inner core implementation of filter function
def myfilter(func,itr):
    res = []
    for i in itr:
        if(func(i)):
            res.append(i)
    return res