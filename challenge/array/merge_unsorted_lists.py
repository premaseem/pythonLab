# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).


def merge_lists(l1, l2):
    sl = []
    while l1 and l2:
        l1e = min(l1)
        l2e = min(l2)

        if l1e < l2e :
            sl.append(l1e)
            l1.remove(l1e)
        else:
            sl.append(l2e)
            l2.remove(l2e)

    if l1:
        sl.extend(l1)
    if l2:
        sl.extend(l2)
    return sl




l1 = [10,76,100,2,4,6,8]
l2 = [3,5,7,8,9]
print(merge_lists(l1,l2))

###################
# In place merge list
def divide(l):
    if len(l) <= 1 :
        return l[:]
    m = len(l) // 2

    l1 = divide(l[:m])
    l2 = divide(l[m:])

    return merge_lists(l1,l2)

print(divide([4,2,6,8,1,90,54,23]))
# merge - divide in l and r


l1 = [2,4,6,8]
l2 = [3,5,7,8,9]
# print(merge_lists_inplace(l1,l2))
