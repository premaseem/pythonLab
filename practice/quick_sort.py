# Quick sort is also called partition sort

a = [19, 13, 3, 10, 4, 5, 7, 80, 32]
print(a)
print(sorted(a))
# size
s = len(a)

def sort(a):
    if len(a) <= 1:
        return a
    return sort([v for v in a if v < a[-1]]) + [a[-1]] + sort([v for v in a if v > a[-1]])

print(sort(a))
# print(a)