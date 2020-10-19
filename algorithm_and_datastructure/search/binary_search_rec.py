lst = [1, 3, 4, 5, 4, 3, 2, 7, 8, 6, 34, 32, 12, 76, 78, 34, 32, 87]
lst = sorted(lst)

# Search with start / end index and original list reference
def binary_search_rec(n, s, e, l):
    if s > e:
        return f"{n} element not found"
    m = (s + e) // 2
    c = l[m]
    if n == c:
        return f"{n} element found at {m}"
    elif n > c:
        return binary_search_rec(n, m + 1, e, l)
    else:
        return binary_search_rec(n, s, m - 1, l)


print(binary_search_rec(51, 0, len(lst), lst))

# Search without start / end index and copy of list using slice
def binary_search_rec_2(n, l):
    start = 0
    end = len(l) - 1
    mid = start + end // 2
    if len(l) < 1:
        return "value not found"
    if n == l[mid]:
        return "value found"
    if n < l[mid]:
        return binary_search_rec_2(n, l[0:mid - 1])
    else:
        return binary_search_rec_2(n, l[mid + 1: len(l)])


print(binary_search_rec_2(1, lst))
