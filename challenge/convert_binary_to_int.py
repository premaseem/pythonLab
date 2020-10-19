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

# reverse string and calculate
def sol(bs):
    p = 0
    n = 0
    bs = bs[::-1]
    for ch in bs:
        l1 = (2 ** p) * int(ch)
        n += l1
        p += 1
        # print(p, l1 , n)
    return n

assert  242 == sol("11110010")
assert  242 == sol1("11110010")
assert  242 == sol2("11110010")
