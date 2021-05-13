'''
Suppose we have an unsorted log file of accesses to web resources. Each log entry consists of an access time, the ID of the user making the access, and the resource ID. 

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

'''

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

# approach 1
# we have 2 d array
# iterate over it, and transformtion into a map/dict "Username" : [first and last access time.]

# def process(l):
#     m = {}
#     for r in l:
#         m.setdefault(r[1],[])
#         m.get(r[1]).append(int(r[0]))

#     fm = {}
#     for k,v in m.items():
#         arr = sorted(v)
#         fm[k] = [arr[0],arr[-1]]

#     print(fm)

# process(logs2)

# approach 2
# transform the data in map k=rousourcename, v = list of time stamps
# find the 300 sec window and count items to find max

def freq_sort(k,lst):
    lst.sort()
    freq_lst = []
    for i,num in enumerate(lst):
        freq = 0
        for x in range(i,len(lst)):
            if lst[x] <= (num + 300):
                freq += 1
        freq_lst.append(freq)

    hf = max(freq_lst)
    si = freq_lst.index(hf)
    ei = si+hf


    return k,hf, freq_lst, lst[si:ei],




def process(l):

    m = {}
    for r in l:
        m.setdefault(r[2],[])
        m.get(r[2]).append(int(r[0]))
    # print(m)
    ans = []
    for k,v in m.items():
        ans.append(freq_sort(k,v))
    ans.sort(key=lambda x:x[1],reverse=True)
    fa = ans[0]
    print("Ans is",fa )
    #most_requested_resource(logs1) # => ('resource_3', 3)
    print("Reason:", fa[0], "is accessed ", fa[1],"times", "at", fa[-1])

process(logs1)
