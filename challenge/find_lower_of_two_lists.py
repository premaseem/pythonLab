# Given: 2 unequal length list, populate 3rd list with lower element of the two in sorted order
a  = [2,9,4]
b  = [3,5,10,3,7]
a = sorted(a)
b = sorted(b)

r = [ n1 if n1 < n2 else n2 for n1,n2 in zip(a,b)]
d = []
if len(a) > len(b):
    d = a[len(b): len(a)]
else:
    d = b[len(a): len(b)]
print("delta",d)
r.extend(d)
print("final result",r)