# optimized bubble sort to do minimum number of iteration

l = [10,9,4,7,2,4]
# l = [1,2,3,4,5]
e = [2,4,4,7,9,10]

itr = 1
swap_happened = True
while swap_happened:
    swap_happened = False
    print("iternation \t", itr, l)
    itr += 1
    for i in range(len(l) - 1):
        if (l[i] > l[i + 1]):
            l[i], l[i + 1] = l[i + 1], l[i]
            swap_happened = True

print("Is sorted properly", e == l)