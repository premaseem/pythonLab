lst = [1,21,3,14,5,60,7,6]
k = 22

lst.sort()
print(lst)
i = 0
j = len(lst)-1
print(i,j)
while i < j:
    total = lst[i] + lst[j]
    if  total == k:
        print( lst[i], lst[j])
        break
    elif total < k:
        i += 1
    else: j -= 1





