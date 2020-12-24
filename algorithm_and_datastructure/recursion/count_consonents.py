# Given a string, calculate the number of consonants present.

s = "Welcome to Educative!"
v = ["a","e","i","o","u"]


def count_consonants_iter():
    num = 0
    for c in s:
        if c.lower() not in v and c.isalpha():
            num += 1
    return num

def rec(s, i=0):
    if i == len(s):
        return 0
    if s[i].lower() not in v and s[i].isalpha():
        return 1 + rec(s,i+1)
    else:
        return rec(s, i+1)


print(count_consonants_iter())
print(rec(s))


