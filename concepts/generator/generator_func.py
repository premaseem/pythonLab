# when fun has yield instead of return it becomes generator function and returns iterator

def num_series(n):
    for i in range(1,n+1):
        yield i


series =num_series(10)
# get next item in iterator fun
print(next(series))

# iterating all items
for item in num_series(5):
    print(item)