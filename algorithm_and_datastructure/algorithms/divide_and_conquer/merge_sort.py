"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""

input = [4,2,8,3,9,1]
expected = [1, 2, 3, 4, 8, 9]

def merge1(l1,l2):
    r = []
    while l1 and l2:
        if l1[0] <= l2[0]:
            r.append(l1.pop(0))
        else :
            r.append(l2.pop(0))

    r.extend(l1)
    r.extend(l2)
    return r

def merge(l1,l2):
    i,j=0,0
    r=[]
    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            r.append(l1[i])
            i += 1 
        else :
            r.append(l2[j])
            j += 1 
    r.extend(l1[i:])
    r.extend(l2[j:])
    return r
        

l1 = [2,4,6,8]
l2 = [3,6,9,12]

print(merge(l1,l2))


def merge_sort(l):
    if len(l) <= 1:
        return l

    pivot = len(l)//2
    ll = merge_sort(l[:pivot])
    rl = merge_sort(l[pivot:])
    return merge(ll,rl)

assert expected == merge_sort(input)

