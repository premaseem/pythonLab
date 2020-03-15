# There are N students in a class.
# Some of them are friends, while some are not.
# Their friendship is transitive in nature, i.e., if A is friend of B and B is friend of C, then A is also friend of C.
# A friend circle is a group of students who are directly or indirectly friends.
#
# You are given a N×N - matrix M which consists of characters Y or N.
# If M[i][j]=Y, then ith and jth students are friends with each other, otherwise not.
# You have to print the total number of friend circles in the class.
#
# Each element of matrix friends will be Y or N.
# Number of rows and columns will be equal in the matrix.
#
# M[i][i]=Y, where 0=i<N
# M[i][j] = M[j][i], where 0=i<j<N
#
# Example 1

# Input:
# YYNN
# YYYN
# NYYN
# NNNY
# Output: 2
#
# Example 2

# Input
# YNNNN
# NYNNN
# NNYNN
# NNNYN
# NNNNY
# Output: 5

# ALGO :
# 1. populate the values in matrix
# find disjoin circle and increment the number
i1 = ["YYNN","YYYN","NYYN","NNNY"]
i2 = ["YNNNN","NYNNN","NNYNN","NNNYN","NNNNY"]

def get_friend_circles(a):
    m=[]
    for e in a:
        m.append(list(e))

    for r in m:
        print(r)

    fg=[]
    for r,e in enumerate(m):
        fs = set()
        fs.add(r)
        for c,ee in enumerate(e):
            if ee is "Y":
                fs.add(c)
        fg.append(fs)
    print(fg)

    for i in range(len(fg)):
        for j in range(i,len(fg)):
            if fg[i].intersection(fg[j]):
                fg[i] = fg[i].union(fg[j])

    print(fg)

    for i in range(len(fg)-1,-1,-1):
        for j in range(len(fg)-1,-1,-1):
            if fg[i].intersection(fg[j]):
                fg[i] = fg[i].union(fg[j])
    print(fg)
    final_set = set()
    for grp in fg:
        grp = [str(e) for e in grp]
        final_set.add("".join(grp))

    print(final_set)

    return len(final_set)

get_friend_circles(i1)
assert get_friend_circles(i1) is 2
assert get_friend_circles(i2) is 5