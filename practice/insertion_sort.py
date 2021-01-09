a = [19, 13, 3, 10, 4, 5, 7, 80, 32]
print(a)
for i in range(1,len(a)-1):
    j=i
    while j >= 0 and a[j] > a[j+1]:
        a[j+1],a[j] = a[j], a[j+1]
        j -= 1

print(a)

a = [19, 13, 3, 10, 4, 5, 7, 80, 32]
print(a)
for i in range(1,len(a)):
    insertion_key = a[i]
    j = i -1
    while j >= 0 and a[j] > insertion_key:
        a[j+1] = a[j]
        j -= 1
    a[j+1] = insertion_key
print(a)