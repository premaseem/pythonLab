

input1 = [
    [[5, 7], [30, 31]],           # device 1
    [[6, 8], [10, 12], [31, 34]], # device 2
    [[6, 7], [9, 10]]             # device 3
    # [[100, 250], [900, 1000000]], # device 4
]

# output: [[5, 8], [9, 12], [30, 34]]

r = []
for e in input1:
    r.extend(e)
print(r)

r.sort(key = lambda e : e[0])
print("sorted",r)


window = r[0]
nw = []
ans = []
i = 1
while i < len(r):
    merge_tuple = [window]
    for j in range(i, len(r)):
        if window[0] <= r[j][0] and r[j][0] <= window[1]:
            merge_tuple.append(r[j])
            i+=1
        else:
            nw = window[::]
            window = r[j]
            break
    if merge_tuple:
        low = merge_tuple[0][0]
        high = max([x[1] for x in merge_tuple ])
        ans.append([low, high])
    else:
        ans.append(nw[0])

print(ans)

































