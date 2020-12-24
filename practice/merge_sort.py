a = [19, 13, 3, 10, 4, 5, 7, 80, 32]
print(a)
print(sorted(a))
# size
s = len(a)


def merge(l, r):
    arr = []
    li, ri = 0, 0
    while li < len(l) and ri < len(r):
        if l[li] <= r[ri]:
            arr.append(l[li])
            li += 1
        else:
            arr.append(r[ri])
            ri += 1

    if li < len(l):
        arr.extend(l[li:])

    if ri < len(r):
        arr.extend(r[ri:])

    return arr


def sort(a):
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = sort(a[:mid])
    right = sort(a[mid:])
    return merge(left, right)


print(sort(a))
