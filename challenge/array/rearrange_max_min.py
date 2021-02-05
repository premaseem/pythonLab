"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Rearrange Sorted List in Max/Min Form
Arrange elements in such a way that the maximum element appears at first position, then minimum at second, then second maximum at third and second minimum at fourth and so on.
"""

i = [1,2,3,4,]
e = [4,1,3,2]


def sol1(lst):
    a = []
    while lst:
        mx = max(lst)
        lst.remove(mx)
        a.append(mx)

        if lst:
            mn = min(lst)
            a.append(mn)
            lst.remove(mn)
    return a
def sol2(lst):
    lst.sort()
    a = []
    l = 0
    r = len(lst)-1

    while l <= r:
        a.append(lst[r])
        r -= 1

        if l <= r:
            a.append(lst[l])
            l += 1
    print(a)
    return a

def sol3(lst):
    # Return empty list for empty list
    if (len(lst) is 0):
        return []

    maxIdx = len(lst) - 1  # max index
    minIdx = 0  # first index
    maxElem = lst[-1] + 1  # Max element
    # traverse the list
    for i in range(len(lst)):
        # even number means max element to append
        if i % 2 == 0:
            lst[i] += (lst[maxIdx] % maxElem) * maxElem
            maxIdx -= 1
        # odd number means min number
        else:
            lst[i] += (lst[minIdx] % maxElem) * maxElem
            minIdx += 1

    print(lst)
    for i in range(len(lst)):
        lst[i] = lst[i] // maxElem
    print(lst)
    return lst


# print(max_min([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))


assert e == sol3(i)
# assert e == sol2(i)
# assert e == sol1(i)
