l = [4, 8, 3, 9, 2]
e = [2, 3, 4, 8, 9]

size = len(l)
# print(size)


# Run a nested loop
size = len(l) - 1
for x in range(0, size):
    for y in range(0, size-x):

        if l[y] > l[y + 1]:
            print(x, y)
            l[y], l[y + 1] = l[y + 1], l[y]

print(l)
print("Is sorted properly", e == l)
