# Binary Search
# find if element is in the sorted list

lst = [1, 3, 4, 5, 7, 8, 32]


def binary_search_recursive(a, e, l, r):
    if r < l:
        print("not found")
        return -1

    m = (l + r) // 2
    if e == a[m]:
        print("found at", m)
        return m

    if e < a[m]:
        r = m - 1
    else:
        l = m + 1
    return binary_search_recursive(a, e, l, r)


print(binary_search_recursive(lst, 1, 0, len(lst)))


def binary_search_iterative(a, e, l, r):
    while l <= r:
        m = (l + r) // 2
        if e == a[m]:
            return m
        if e > a[m]:
            l = m + 1
        else:
            r = m - 1
    else:
        print("Not found")
        return -1


print(binary_search_iterative(lst, 5, 0, len(lst)))


# Search without start / end index and copy of list using slice, without returning index
def binary_search_recursive_slice(a, e):
    if len(a) <= 0 :
        return -1
    m = len(a) // 2

    if a[m] == e:
        return "found"

    if e < a[m]:
        a = a[:m]
    else: a = a[m+1:]

    return binary_search_recursive_slice(a,e)

print(binary_search_recursive_slice(lst, 32))
