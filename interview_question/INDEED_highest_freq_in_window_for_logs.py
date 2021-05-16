"""
@Author: Aseem Jain
@Linkedin: https://www.linkedin.com/in/premaseem/
@Github: https://github.com/premaseem/pythonLab/tree/master/challenge

'''
Suppose we have an unsorted log file of accesses to web resources.
Each log entry consists of an access time, the ID of the user making the access, and the resource ID.

The access time is represented as seconds since 00:00:00, and all times are assumed to be in the same day.

For example:
logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    ["54359", "user_1", "resource_3"],
]

Example 2:
logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]



Write a function that takes the logs and returns the resource with the highest number of accesses in any 5 minute window, together with how many accesses it saw.

Expected Output:
most_requested_resource(logs1) # => ('resource_3', 3)
Reason: resource_3 is accessed at 53760, 54001, and 54060

most_requested_resource(logs2) # => ('resource_3', 4)
Reason: resource_3 is accessed at 1199, 1200, 1201, and 1202

Complexity analysis variables:

n: number of logs in the input

"""

logs1 = [
    ["58523", "user_1", "resource_1"],
    ["62314", "user_2", "resource_2"],
    ["54001", "user_1", "resource_3"],
    ["200", "user_6", "resource_5"],
    ["215", "user_6", "resource_4"],
    ["54060", "user_2", "resource_3"],
    ["53760", "user_3", "resource_3"],
    ["58522", "user_22", "resource_1"],
    ["53651", "user_5", "resource_3"],
    ["2", "user_6", "resource_1"],
    ["100", "user_6", "resource_6"],
    ["400", "user_7", "resource_2"],
    ["100", "user_8", "resource_6"],
    [ "54359", "user_1", "resource_3"],
]

logs2 = [
    ["300", "user_1", "resource_3"],
    ["599", "user_1", "resource_3"],
    ["900", "user_1", "resource_3"],
    ["1199", "user_1", "resource_3"],
    ["1200", "user_1", "resource_3"],
    ["1201", "user_1", "resource_3"],
    ["1202", "user_1", "resource_3"]
]


# Analyze logs and output first and last access time for each user

"""
1. Transform list into map with user as key and list of ts as value 
2. Data massage, sort the list and grab first and last ts
3. return or print
"""

def sol1(lst):
    print(lst)
    m = {}
    for r in lst:
        m.setdefault(r[1],[])
        m[r[1]].append(int(r[0]))
    print(m)
    fm = {}
    for k,v in m.items():
        v.sort()
        fm[k] = [v[0],v[-1]]
    print("final map as answer", fm)
    return fm


sol1(logs1)


# Coding Challenge to analyze logs and output access timestamp in 5 minute window

# => ('resource_3', 3)
# Reason: resource_3 is accessed at 53760, 54001, and 54060

# Algo
"""
1. Transform to map k: resource_id v: list of timestamps
2. Sort the timestamps and calculate the frequence in 5 min window 
3. return the highest access resource. 
"""

def freq(lst):
    ansl = []
    for x in lst:
        deltaList = []
        for y in lst:
            if y >= x and y <= (x + 300):
                deltaList.append(y)
        ansl.append(deltaList)
    ml = 0
    mi = 0
    for i,r in enumerate(ansl):
        if ml <= len(r):
            ml = len(r)
            mi = i
    print(ansl)
    ansl.append(ml)
    ansl.append(mi)
    return ansl

# def find_max(lst):


def most_requested_resource(l):
    print(l)
    m = {}
    for r in l:
        m.setdefault(r[2],[])
        m[r[2]].append(int(r[0]))
    print(m)

    fm = {}
    for k,v in m.items():
        fm[k] = freq(v)

    print(fm)
    ans = 0
    itms = None
    resource = None
    for k,v in fm.items():
        if ans <= v[-2]:
            ans = v[-2]
            itms = v[v[-1]]
            resource = k
    # => ('resource_3', 3)
    # Reason: resource_3 is accessed at 53760, 54001, and 54060
    print(f"Reason: {resource} is accessed max frequency of {ans} with ts {itms}")





most_requested_resource(logs1)




