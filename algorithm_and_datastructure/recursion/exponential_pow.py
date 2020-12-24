
def pow(b,e):
    if e == 0:
        return 1
    return b * pow(b,e-1)

assert 4 == pow(2,2)
assert 1024 == pow(2,10)