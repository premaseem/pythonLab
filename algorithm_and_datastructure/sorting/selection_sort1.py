l = [10,9,4,7,2,4]
# l = [1,2,3,4,5]
e = [2,4,4,7,9,10]


for x in range(len(l)):
    print(f"running for position {x} :{l}")
    for y in range(x,len(l)):
        if l[x] > l[y]:
            l[x], l[y] = l[y], l[x]

print("Is sorted properly", e == l, l)