a = [19, 13, 3, 10, 4, 5, 7, 80, 32]

# size
s = len(a)

swapped = True
while swapped:
    swapped = False
    for i in range(s):
        for j in range(s - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True

print(a)

a = [19, 13, 3, 10, 4, 5, 7, 80, 32]

# brute force / prem sort
for i in range(s):
    for j in range(i, s):
        if a[i] > a[j]:
            a[i], a[j] = a[j], a[i]

print(a)
