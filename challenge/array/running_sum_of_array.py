"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/
Running Sum of 1d Array
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


"""

# Input:
nums = [3,1,2,10,1]
Output = [3,4,6,16,17]


def sol1(nums):
    ans = []
    for i in range(len(nums)):
        ans.append(sum(nums[:i+1]))
    return ans

def sol2(nums):
    return [sum(nums[:i+1]) for i in range(len(nums))]

def sol3(nums):
    ans = [nums[0]]
    for i in range(1,len(nums)):
        ans.append(nums[i]+ans[i-1])
    return ans

def sold4(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums

assert Output == sol1(nums)
assert Output == sol2(nums)
assert Output == sol3(nums)
assert Output == sol3(nums)
