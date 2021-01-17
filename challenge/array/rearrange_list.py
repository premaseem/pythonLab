"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Implement a function rearrange(lst) which rearranges the elements such that all the negative elements appear on the left and positive elements appear at the right of the list.
Note that it is not necessary to maintain the sorted order of the input list

"""


i = [10,-1,20,4,5,-9,-6]
e = [-1,-9,-6,10,20,4,5]

def sol(lst):
    na = []
    for e in lst:
        if e < 0:
            na.insert(0,e)
        else:
            na.append(e)
    print(na)
    return na

def sol1(lst):
    l1 = []
    l2 = []
    for e in lst:
        if e < 0:
            l1.append(e)
        else:
            l2.append(e)
    l = l1 + l2
    print (l)
    return l1 + l2


def sol3(lst):
    leftMostPosEle = 0  # index of left most element
    # iterate the list
    for curr in range(len(lst)):
        # if negative number
        if (lst[curr] < 0):
            # if not the last negative number
            if (curr is not leftMostPosEle):
                # swap the two
                lst[curr], lst[leftMostPosEle] = lst[leftMostPosEle], lst[curr]
            # update the last position
            leftMostPosEle += 1
    return lst

# Two pointer approach
def sol4(lst):

    lp=0
    rp=len(lst)-1

    while lp < rp:
        while lst[lp] < 0 :
            lp += 1
        while lst[rp] > 0 :
            rp -= 1
        if lp < rp:
            lst[lp], lst[rp] = lst[rp], lst[lp]

        print(lst)

    return lst




# assert e == sol1(i)
assert e == sol4(i)
