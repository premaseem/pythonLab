"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""


def sol(n):
    return n * 2


test_data = [
    (2, 4),
    (4, 8),
]

for given, expected in test_data:
    assert expected == sol(given)
    print(f"Test passed for: given {given} and expected = {expected}")
