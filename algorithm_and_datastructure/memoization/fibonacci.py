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

def fib( N: int) -> int:
    memo = {0:0, 1:1}
    def dfs(n):
        if n not in memo: memo[n] = dfs(n-1)+dfs(n-2)
        return memo[n]


    return dfs(N)



assert 3 == fib(4)
assert 2 == fib(3)
assert 1 == fib(2)