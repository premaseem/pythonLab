l = [n for n in range(10)]
print(l)

# Generator comprehension
g = (n for n in range(10))
print(g)
print(list(g))


def my_generator(num):
    for n in range(num):
        yield n

print(my_generator(25))
