"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

First Non-Repeating Integer in a list
Given a list, find the first integer which is unique in the list. Unique means the number does not repeat and appears only once in the whole list. Implement your solution in Python and see if it runs correctly!
"""

i = [2,3,2,6,6]
e = 3

def brut(l):
    for i in range(len(l)):
        pair = False
        for j in range(len(l)):
            if i != j:
                if l[i] == l [j]:
                    pair = True
                    break
        if not pair:
            return l[i]

def counter(l):
    for e in l:
        if l.count(e) == 1:
            print(e)
            return e

def popper(l):
    for e in l:
        l.remove(e)
        if e not in l:
            return e

def sol(l):
    m = {}
    for e in l:
        if e in m:
            m[e] = e
        else:
            m[e] = None

    for k,v in m.items():
        if not v:
            return k

assert e == brut(i)
assert e == counter(i)
assert e == sol(i)
# assert e == popper(i)

