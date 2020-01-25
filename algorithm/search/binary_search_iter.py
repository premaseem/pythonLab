"""
Binary search
"""
import random
lst = [random.randint(0,10000) for i in range(10000)]
lst = [1,3,4,5,4,3,2,7,8,6,34,32,12,76,78,34,32,87]
lst = sorted(lst)

def binary_search_itr(e,l):
    start = 0
    end = len(l)-1

    while end >= start:
        middle = (start + end) // 2
        candidate =  l[middle]
        if e == candidate:
            return f"{e} element found at {middle}"
        elif e < candidate:
            end = middle-1
            print(f"seek range {start} - {end}")
        else:
            start = middle+1
            print(f"seek range {start} - {end}")
    return f"{e} element not found"

print(binary_search_itr(1,lst))

