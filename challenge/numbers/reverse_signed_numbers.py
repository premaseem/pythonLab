def sol( x: int) -> int:
    is_neg = x < 0
    rev = str(abs(x))[::-1]
    val = int(rev)
    if val > 2147483647 or val < -2147483647:
        return 0
    if is_neg:
        return  -1 * val
    return val

def sol1(n):
    m = -1 if n < 0 else 1
    n = abs(n)
    ans = 0
    while n > 0:
        ans *= 10
        r = n % 10
        n = n // 10
        ans += r
    return m * ans


test_data = [
    (123 ,321),
    (-1234 ,-4321),
    (0 ,0),
    (100 ,1),
]
for given, expected in test_data:
    assert expected == sol(given)
    assert expected == sol1(given)
    print(f"Test passed for: given {given} and expected = {expected}")
