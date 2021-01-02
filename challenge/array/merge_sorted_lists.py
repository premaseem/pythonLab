# Implement a function that merges two sorted lists of m and n elements respectively, into another sorted list. Name it merge_lists(lst1, lst2).


def merge_lists(l1,l2):
    sl = [0]
    while l1 and l2:
        if l1[0] <= l2[0]:
            sl.append(l1.pop(0))
        else:
            sl.append(l2.pop(0))
    if l1:
        sl.extend(l1)
    if l2:
        sl.extend(l2)
    return sl[1:]


l1 = [2,4,6,8]
l2 = [3,5,7,8,9]
print(merge_lists(l1,l2))

###################
# In place merge list
def merge_lists_inplace(l1,l2):
    li1 = li2 = 0
    while li1 < len(l1) and li2 < len(l2):
        if l1[li1] > l2[li2]:
            l1.insert(li1, l2[li2])
            li2 += 1
        else:
            li1 += 1
    l1.extend(l2[li2:])
    return l1

l1 = [2,4,6,8]
l2 = [3,5,7,8,9]
print(merge_lists_inplace(l1,l2))
