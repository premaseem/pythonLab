l = [4,6,8]
r = [3,6,9,12]

# merge and for a new sorted list

def merge(l,r):

    li=0
    ri =0
    ls = len(l)
    rs = len(r)
    fs = ls + rs
    f = [None] * fs
    for i in range(fs):

        # picking left list
        if li < ls:
            if ri < rs:
                if l[li] < r[ri]:
                    f[i] = l[li]
                    li += 1
                    continue
                else:
                    f[i] = r[ri]
                    ri += 1
                    continue
            else:
                f[i] = l[li]
                li += 1
                continue

        if ri < rs:
            if li < ls:
                if r[ri] < l[li]:
                    f[i] = r[ri]
                    ri += 1
                    continue
                else:
                    f[i] = l[li]
                    li += 1
                    continue
            else:
                f[i] = r[ri]
                ri += 1
                continue

    return f
ans = merge(l,r)
print(ans)
