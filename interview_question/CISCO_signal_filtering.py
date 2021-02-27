# ON = 1
# OFF = 0
# [[5, ON], [7, OFF], [30, ON], [31, OFF], [36, ON]]

# 0         5   7                                             30 31          36
# + + + + + + - - + + + + + + + + + + + + + + + + + + + + + + +  - + + + + +

# input: [[5, ON], [7, OFF], [30, ON], [31, OFF], [36, ON]]
# output: [[5,7], [30,31]]

def sol(lst):
    r = []
    t = []
    if lst[0][1] == "OFF":
        t = [0]

    for event in lst:
        if event[1] == "ON":
            t.append(event[0])
            continue
        if event[1] == "OFF":
            t.append(event[0])
            r.append(t)
        t = []
    return r

def sol2(lst):
    r = []
    t = [0] if lst[0][1] == "OFF" else []

    for event in lst:
        t.append(event[0])
        if event[1] == "OFF":
            r.append(t)
            t = []

    return r

def sol3(lst):
    """ fix the input if not expected """
    r = []
    e = []
    if lst[0][1] != "ON":
        lst.insert(0,[0,"ON"])

    for i, (tm,st) in enumerate(lst):
        e.append(tm)
        if i % 2 == 1:
            r.append(e)
            e = []
    return r

inputOff = [[3, "OFF"], [5, "ON"], [7, "OFF"], [30, "ON"], [31, "OFF"], [36, "ON"]]
inputon = [[5, "ON"], [7, "OFF"], [30, "ON"], [31, "OFF"], [36, "ON"]]

expectedOff = [[0, 3], [5, 7], [30, 31]]
expected = [[5,7], [30,31]]

td = [(inputOff,expectedOff),
      (inputon, expected)
      ]

for given,expected in td:
    assert expected == sol(given)






























