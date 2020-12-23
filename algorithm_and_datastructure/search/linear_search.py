# Linear Search

a = [1, 3, 4, 5, 7, 8, 32]

# element to search
e = 3

# for loop
for i in range(len(a)):
    if a[i] == e:
        print("found")
        break
else:
    print("not found")

# while loop
i = 0
while i < len(a):
    if a[i] == e:
        print("found")
        break
    i += 1
else:
    print("not found")
