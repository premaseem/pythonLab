# Reverse the given string

def sol1(s):
    return s[::-1]


def sol2(s):
    ra =[]
    size = len(s)
    for i in range(size):
        ra.append(s[size -1 - i])
    return "".join(ra)

def sol3(s):
    rev = ""
    for i in range(len(s) - 1, -1, -1):
        rev += s[i]
    return rev


# tests

assert "meesa" == sol1("aseem")
assert "meesa" == sol2("aseem")
assert "meesa" == sol3("aseem")
assert "!evitacudE ot emocleW" == sol1("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol2("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol3("Welcome to Educative!")
