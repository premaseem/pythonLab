# Exercise: Product of Two Positive Integers

def itr(a,b):
    p = 0
    for i in range(a):
        p += b
    return p

assert 32 == itr(8,4)

def rec(a,b,cnt=0):
    if cnt == a:
        return 0
    return b + rec(a,b,cnt+1)

assert 32 == rec(8,4)

def rec2(a,b):
    # This cuts down on the total number of
    # recursive calls:
    if b > a:
        rec2(b,a)

    if b == 0 :
        return 0
    return a + rec2(a,b-1)

assert 32 == rec2(4,8)