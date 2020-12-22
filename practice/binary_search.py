lst = [1, 3, 4, 5, 4, 3, 2, 7, 8, 6, 34, 32, 12, 76, 78, 34, 32, 87]
lst = sorted(lst)

# find if element is in the sorted list
e = len(lst)
b = 0
n = -8
while True:
    mi = (b + e) // 2
    if lst[mi] == n :
        print("found", n, "@",mi)
        break
    if mi < 0 or mi > len(lst) or mi == b or mi == e:
        print("not found")
        break
    b = mi if n > lst[mi] else mi +1


def fun(n,a,b,e):
    mi = (b+e)//2
    if n == a[mi]:
        print("found ", n , "@", mi )
        return mi
    if mi < 0 or mi > len(a)-1:
        print("not found")
        return -1
    if b == e:
        print("not found")
        return -1
    if n < a[mi]:
        ans = fun(n,a,b,mi)
    elif n > a[mi]:
        ans = fun(n,a,mi+1,e)
    return ans

# print(fun(8,lst,0,len(lst)))