"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/


Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].
"""

target = 9
nums = [2,7,11,15]
expected = [0,1]

def sol(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if target == nums[i] + nums[j]:
                return [i,j]

# two pointer approach
def sol1(nums,target):
    nums_s = sorted(nums)
    i,j = 0, len(nums_s)-1
    while i < j:
        total = nums_s[i] + nums_s[j]
        if target == total:
            break
        if total < target:
            i += 1
        else:
            j -= 1

    return [ nums.index(nums_s[i]),nums.index(nums_s[j])]

def sol2(nums,target):
    mm = {}
    for i, num in enumerate(nums):
        if num in mm:
            return [i, mm[num]]
        mm[target-num] = i



assert expected == sol(nums,target)
# assert expected == sol1(nums,target)
assert [2,1] == sol2([3,2,4],6)