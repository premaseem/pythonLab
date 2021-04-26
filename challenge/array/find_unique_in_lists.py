"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""
a = [15, 4, 3, 7,9,9, 8, 45]
b = [4, 5, 13, 7, 45, 8]

def sol(a,b):
    """Brute force """
    unique = []
    for x in a:
        if x not in b and x not in unique:
            unique.append(x)

    for x in b:
        if x not in a and x not in unique:
            unique.append(x)

    return unique

def sol1(a,b):
    unique = a.copy()
    unique.extend(b)
    ans = set(unique)
    print("sol1",ans)
    intr = set(a).intersection(b)
    intr.re
    f = ans - intr
    return f


print(sol(a,b))

test_data = [
    ((a,b), [15, 3, 9, 5, 13])
]

for given, expected in test_data:
    print(f"Testing with: given {given} and expected = {expected}")
    assert expected == sol(given[0],given[1])
    assert expected == sol1(given[0],given[1])
