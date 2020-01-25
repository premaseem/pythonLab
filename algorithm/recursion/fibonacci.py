def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo(n-1) + fibo(n-2)

def iter(n):
    a,b = 0,1
    for x in range(n):
        a,b = b,a+b
    return a
print(iter(1))