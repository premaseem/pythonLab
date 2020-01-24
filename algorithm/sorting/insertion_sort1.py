l = [10, 9, 4, 7, 2, 4]
# l = [1,2,3,4,5]
e = [2, 4, 4, 7, 9, 10]

index = 1
for index in range(1, len(l)):
    print(f"iteration for {index} : {l}")

    for x in range(index, 0, -1):
        if l[x] < l[x - 1]:
            l[x], l[x - 1] = l[x - 1], l[x]

print("Is sorted properly", e == l, l)
