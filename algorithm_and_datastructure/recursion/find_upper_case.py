# The algorithm should return P L, and output a message indicating that no capital letter was found for str_1, str_2, and str_3, respectively.

str_1 = "lucidProgramming"
str_2 = "LucidProgramming"
str_3 = "lucidprogramming"

def find_upper_i(s,i=0):
    if len(s)-1 == i:
        return "no upper case"
    if s[i].isupper():
        return s[i]
    return find_upper_i(s,i+1)

print(find_upper_i(str_1))
print(find_upper_i(str_2))
print(find_upper_i(str_3))


def find_upper_r(s,a):
    if len(s) == 0:
        return
    if s[0].isupper():
        a.append(s[0])
    find_upper_r(s[1:],a)
    if not a:
        return "no upper case"
    return a

print(find_upper_r(str_1,[]))
print(find_upper_r(str_2,[]))
print(find_upper_r(str_3,[]))




# iterative
def find_upper(s):
    l=[c for c in s if c.isupper()]
    if not l:
        return "no upper case chars"
    return l

print(find_upper(str_1))
print(find_upper(str_2))
print(find_upper(str_3))
