# Convert Binary to Decimal Integer

def sol1(bs):
    f = 0
    p = 0
    for i in range(len(bs)):
        f += 2 ** p * int(bs[len(bs)-1-i])
        p += 1
    return f

def sol2(b):
    f = 0
    p = 0
    b = list(b)
    while len(b):
        f += 2 ** p * int(b.pop())
        p += 1
    return f

assert  242 == sol1("11110010")
assert  242 == sol2("11110010")
