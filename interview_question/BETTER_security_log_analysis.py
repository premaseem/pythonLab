"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

We are working on a security system for a badged-access room in our company's building.

Given an ordered list of employees who used their badge to enter or exit the room,
write a function that returns two collections:

1. All employees who didn't use their badge while exiting the room
- they recorded an enter without a matching exit.
(All employees are required to leave the room before the log ends.)

2. All employees who didn't use their badge while entering the room
- they recorded an exit without a matching enter.
(The room is empty when the log begins.)

Each collection should contain no duplicates,
regardless of how many times a given employee matches the criteria for belonging to it.

badge_records_1 = [
  ["Martha",   "exit"],
  ["Paul",     "enter"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "enter"],
  ["Paul",     "enter"],
  ["Curtis",   "exit"],
  ["Curtis",   "enter"],
  ["Paul",     "exit"],
  ["Martha",   "enter"],
  ["Martha",   "exit"],
  ["Jennifer", "exit"],
  ["Paul",     "enter"],
  ["Paul",     "enter"],
  ["Martha",   "exit"],
]

Expected output: ["Curtis", "Paul"], ["Martha", "Curtis"]

Additional test cases:

badge_records_2 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], []

badge_records_3 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: [], ["Paul"]

badge_records_4 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
  ["Martha", "enter"],
  ["Martha", "exit"],
]

Expected output: ["Paul"], ["Paul"]

badge_records_5 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
]

Expected output: [], []

badge_records_6 = [
  ["Paul", "enter"],
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
]

Expected output: ["Paul"], ["Paul"]

badge_records_7 = [
  ["Paul", "enter"],
  ["Paul", "exit"],
  ["Paul", "exit"],
  ["Paul", "enter"],
]

Expected output: ["Paul"], ["Paul"]


n: length of the badge records array

"""

badge_records_1 = [
    ["Martha",   "exit"],
    ["Paul",     "enter"],
    ["Martha",   "enter"],
    ["Martha",   "exit"],
    ["Jennifer", "enter"],
    ["Paul",     "enter"],
    ["Curtis",   "exit"],
    ["Curtis",   "enter"],
    ["Paul",     "exit"],
    ["Martha",   "enter"],
    ["Martha",   "exit"],
    ["Jennifer", "exit"],
    ["Paul",     "enter"],
    ["Paul",     "enter"],
    ["Martha",   "exit"],
]

badge_records_2 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
]

badge_records_3 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]

badge_records_4 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
    ["Martha", "enter"],
    ["Martha", "exit"],
]

badge_records_5 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
]

badge_records_6 = [
    ["Paul", "enter"],
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
]

badge_records_7 = [
    ["Paul", "enter"],
    ["Paul", "exit"],
    ["Paul", "exit"],
    ["Paul", "enter"],
]


def sol(lst):
    missing_exit = set()
    missing_entry = set()
    d = {}
    for r in lst:
        l = d.setdefault(r[0],[])
        l.append(r[1])

    for k,v in d.items():

        if v.count("enter") > v.count("exit"):
            missing_exit.add(k)

        if v.count("enter") < v.count("exit"):
            missing_entry.add(k)

        if v.count("enter") == v.count("exit"):
            for i, rec in enumerate(v):
                if i % 2 == 0 and rec != "enter":
                    missing_entry.add(k)
                if i % 2 != 0 and rec != "exit":
                    missing_exit.add(k)

    return sorted(missing_exit), sorted(missing_entry)


def sol1(lst):
    missing_exit = set()
    missing_entry = set()
    d = {}
    for r in lst:
        l = d.setdefault(r[0],[])
        l.append(r[1])

    for k,v in d.items():
        exp = "enter"
        for e in v:
            if e != exp and exp == "enter":
                missing_entry.add(k)
            if e != exp and exp == "exit":
                missing_exit.add(k)
            exp = "enter" if e == "exit" else "exit"
        if v[-1] != "exit":
            missing_exit.add(k)

    return sorted(missing_exit), sorted(missing_entry)

test_data = [
    (badge_records_1, ["Curtis", "Paul"], ["Martha", "Curtis"]),
    (badge_records_2, ["Paul"], []),
    (badge_records_3, [], ["Paul"]),
    (badge_records_4, ["Paul"], ["Paul"]),
    (badge_records_5, [], []),
    (badge_records_6, ["Paul"], ["Paul"]),
    (badge_records_7, ["Paul"], ["Paul"]),

]

for given, expected1,expected2 in test_data:
    actual1, actual2 = sol1(given)
    assert (sorted(expected1),sorted(expected2)) == (actual1, actual2)
    print(f"Test passed for: given {actual1} and {actual2} expected = {expected1} and {expected2}")
    print()
