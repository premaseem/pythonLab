"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Fibonacci Number

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.


Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.

"""

def sol(n):
    l = [0,1]
    for i in range(2,n+1):
        l.append(l[i-1]+l[i-2])

    return l[n]

def sol1(n):
    a,b = 0,1
    for i in range(2,n+1):
        c = b + a
        b,a = c,b
    return c


def rec(n):
    if n <= 1:
        return n

    return    memo(n-2) + memo(n-1)

d = {0:0, 1:1}
def memo(n):
    global d
    if not d.get(n):
        for i in range(2,n+1):
            if not d.get(n):
                d[n] = d[n-2]+ d[n-1]
    return d.get(n)


assert 2 == sol1(3)
assert 1 == sol1(2)

assert 2 == rec(3)
assert 1 == rec(2)
