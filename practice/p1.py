# Iterating multiple lists or enumerable objects together, runs to shorted of 2
# lst = [1,2,3,4,6,8]

# nums = [2,0,2,1,1,0]
# for x in range(len(nums)):
#     for y in range(x+1,len(nums)):
#         if nums[y]<nums[x]:
#             print("index",x,y)
#             print(nums[x],nums[y])
#             nums[x],nums[y] = nums[y],nums[x]
#
# print(nums)

lst = [1,2,3,4,6,8,10,14,20,50,100,123,200]

def b_searh(n,lst):
    def srch(n,lst,l,r):
        if l >= r:
            return False
        m = (l + r) // 2
        if n == lst[m]:
            return True
        if n > lst[m]:
            l = m+1
        else:
            r = m-1
        return srch(n,lst,l,r)
    return srch(n,lst,0,len(lst))

print(b_searh(200,lst))