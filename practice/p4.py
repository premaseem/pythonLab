"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

"""


def sol():
    input = [[5, "ON"], [7, "OFF"], [30, "ON"], [31, "OFF"], [36, "ON"]]
    input = [[3, "OFF"],[5, "ON"], [7, "OFF"], [30, "ON"], [31, "OFF"], [36, "ON"]]
    e = [] if input[0][1] == "ON" else [0]
    r = []
    for tm,st in input:
        # print(tm,st)
        e.append(tm)
        if st == "OFF":
            r.append(e)
            e=[]

    print(r)

def sol():
    # input = [[5, "ON"], [7, "OFF"], [30, "ON"], [31, "OFF"], [36, "ON"]]
    input = [[3, "OFF"],[5, "ON"], [7, "OFF"], [30, "ON"], [31, "OFF"], [36, "ON"]]
    r = []
    e = []
    # exp = 1 if input[0][1] == "ON" else 0
    if input[0][1] != "ON":
        input.insert(0,[0,"ON"])
    for i, (tm,st) in enumerate(input):
        e.append(tm)
        if i % 2 == 1:
            r.append(e)
            e = []
    print(r)

sol()

test_data = [
    (2, 4),
    (4, 8),
]

# for given, expected in test_data:
#     assert expected == sol(given)
#     print(f"Test passed for: given {given} and expected = {expected}")
