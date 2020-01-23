# Basically, think of lambda expressions as being 1 time use functions that you create on the fly and discard after use. You don't necessarily name them anything (you can if you want to re-use them but it's not common).
#
# You define a lambda expression with the keyword lambda. For example lambda x: x*2 will return the doubled value of any number you give it (signified by *2). Think of x as the argument being passed in and think of anything to the right of the : being the return value of the function.
#
# If you use the map function in conjunction with a lambda expression on elements of the list defined below, what would the output be?

# Note: Map goes with collection or iterable.
l1 = [2,3,4,5,6]
l1 = list(map(lambda x: x**2, l1))
print(l1)

names = ["sapna", "ranu", "sandhya", "swati", "trishla"]
for n in map(str.capitalize, names):
    print(n)
# print(", ".join(list((map(str.capitalize, names)))))


########################
# creating a custom map
def my_map(f, lst):
    for i in lst:
        yield f(i)

o = my_map(str.capitalize, names)
print(next(o))
print(next(o))
print(list(o))


