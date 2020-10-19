"""
Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].

Return the array in the form [x1,y1,x2,y2,...,xn,yn].

Input: nums = [2,5,1,3,4,7], n = 3
Output: [2,3,5,4,1,7]
Explanation: Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7].

link: https://leetcode.com/problems/shuffle-the-array/

"""
def sol(nums,n):


    temp = n
    insert_position = 1
    for i in range(n):
        nums.insert(insert_position, nums[n])
        n += 2
        insert_position += 2
    del nums[(2*temp):len(nums)]
    return nums



def sol5(l,n):

    def gen():
        for i in range(n):
            yield from (l[i],l[i+n])
    nl = list(gen())
    return nl


def sol4(l,n):
    nl=[]
    for item in zip(l[:n],l[n:]):
        nl.extend(item)
    return nl

def sol3(l,n):
    nl=[]
    for e1,e2 in zip(l[:n],l[n:]):
        nl.append(e1)
        nl.append(e2)
    return nl

def sol2(l,n):
    i=0
    nl=[]
    while i < n:
        nl.append(l[i])
        nl.append(l[n+i])
        i=i+1
    return nl


def sol1(l,n):
    nl = []
    for i in range(len(l)//2):
        nl.append(l[i])
        nl.append(l[n+i])
    return nl

assert [2,3,5,4,1,7] == sol([2,5,1,3,4,7],3)
