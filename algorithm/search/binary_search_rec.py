lst = [1,3,4,5,4,3,2,7,8,6,34,32,12,76,78,34,32,87]
lst = sorted(lst)
def binary_search_rec(n,s,e,l):
    if s > e:
        return f"{n} element not found"
    m = (s + e) // 2
    c = l[m]
    if n == c:
        return f"{n} element found at {m}"
    elif n > c:
        return binary_search_rec(n, m+1,e,l)
    else:
        return binary_search_rec(n, s,m-1,l)

print(binary_search_rec(51,0,len(lst),lst))
