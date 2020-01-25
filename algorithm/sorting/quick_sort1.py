# optimized bubble sort to do minimum number of iteration

l = [10, 9, 4, 7, 2, 4]
# l = [1,2,3,4,5]
e = [2, 4, 4, 7, 9, 10]


def quick_sort(arr):
    if len(arr) < 2:
        return arr[:]
    pivot = arr[-1]
    s, e, l = [], [], []
    for num in arr:
        if num < pivot:
            s.append(num)
        elif num == pivot:
            e.append(num)
        else:
            l.append(num)
    return quick_sort(s) + e + quick_sort(l)

l = quick_sort(l)
print("Is sorted properly", e == l)
