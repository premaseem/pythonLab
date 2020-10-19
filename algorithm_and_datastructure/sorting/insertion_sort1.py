l = [10, 9, 4, 7, 2, 4]
l = [1,2,3,4,5]
e = [2, 4, 4, 7, 9, 10]

index = 1
hits = 1
for index in range(1, len(l)):
    print(f"iteration for {index} : {l}")
    hits += 1
    if(l[index] < l[index -1]): # this if is only for optimization to avoid un necessary iterations
        # we assume all numbers before partition index are already sorted, if number at index greater
        # then consicutive item, there is no point it iterating it further.
        for x in range(index, 0, -1):
            # inner loop iterates to place the lowest element all the way to start.
            hits += 1
            if l[x] < l[x - 1]:
                l[x], l[x - 1] = l[x - 1], l[x]

print("Is sorted properly in hits ", hits, e == l, l)
