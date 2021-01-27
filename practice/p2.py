#Check Permutation: Given two strings,write a method to decide if one is a permutation of the other.

# def sol(s1,s2):
#     if len(s1) != len(s2):
#         return False
#
#     return list(s1).sort() == list(s2).sort()

def sol(s1,s2):
    if len(s1) != len(s2):
        return False
    # implicit map comparision
    # return char_count(s1) == char_count(s2)
    return is_equal(char_count(s1),char_count(s2))

def char_count(s):
    m={}
    for c in s:
        if not m.get(c):
            m[c] = 1
        else:
            m[c] +=1
    print(m)
    return m

def is_equal(m1,m2):
    for k,v in m1.items():
        v2 = m2.get(k)
        if v != v2:
            return False
    return True



assert sol("aseem","seema")
assert not sol("jain","jainz")
assert not sol("jain","hain")