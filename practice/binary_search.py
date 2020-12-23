lst = [1, 3, 4, 5, 7, 8, 32]

# find if element is in the sorted list
e = len(lst)
b = 0
n = 3

while True:
    mi = (b + e) // 2
    if lst[mi] == n :
        print("found", n, "@",mi)
        break
    if mi < 0 or mi > len(lst) or mi == b or mi == e:
        print("not found")
        break

    if n < lst[mi]:
        e = mi -1
    else:b = mi+1



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