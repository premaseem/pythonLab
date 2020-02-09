# Convert Decimal Integer to Binary

def sol1(d):
    ba = []
    f = ""
    while d > 0:
        ba.append(d % 2)
        d = d // 2

    while len(ba):
        f += str(ba.pop())

    print( f)
    return f

assert "11110010" == sol1(242)