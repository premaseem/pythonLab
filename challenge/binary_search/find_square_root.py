t = 300

def sqr(n):
    l = 1
    h = 25
    while l<h:
        print(l,h)
        mid = (l + h) // 2
        sqr = mid * mid
        if sqr <= n:
            l += 1
        else:
            h -= 1
    return l - 1

k = 300
print(sqr(k))






