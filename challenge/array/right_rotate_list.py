"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Implement a function right_rotate(lst, k) which will rotate the given list by k.
This means that the right-most elements will appear at the left-most position in the list and so on. You only have to rotate the list by one element at a time.

"""
i = [10,20,30,40,50,60,70]
n = 3
e = [50,60,70,10,20,30,40]

def right_rotate(lst, k):
    # Write your code here
    return lst[-3:] + lst[:-3]

def brut(lst,k):
    na = []
    for i in range(len(lst)-1,len(lst)-k-1,-1):
        na.append(lst[i])
    for i in range(0,len(lst)-k):
        na.append(lst[i])
    print(na)
    return na

assert e == right_rotate(i,n)