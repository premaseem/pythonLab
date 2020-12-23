a = [19, 13, 3, 10, 4, 5, 7, 80, 32]
print(a)
print(sorted(a))
# size
s = len(a)

for i in range(s):
    lowest_index = i
    for j in range(i+1,s):
        if a[j] < a[lowest_index]:
            # lowest_index = j
            a[j], a[lowest_index] = a[lowest_index],a[j]
    print("pass ", i , a )
    # swap
    a[i], a[lowest_index] = a[lowest_index],a[i]

print(a)

