

def rev(n):
    s=""
    if n < 0:
       s="-"
       n=str(n)[1:]

    r = str(n)[-1::-1]
    while r[0] == "0":
        r=r[1:]
    return int(s+r)

assert 123 == rev(321)
assert -123 == rev(-321)
assert -21 == rev(-120)