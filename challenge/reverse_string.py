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

def sol4(s):
    ans = ""
    l = len(s) -1

    for i, c in enumerate(s):
        ans += s[l-i]
    return ans

def sol5(s):
    s_list = list(s)
    s_list.reverse()
    ans = "".join(s_list)
    return ans

def sol6(s):
    s_l = list(s)
    ans = ""

    while s_l:
        ans += s_l.pop()

    return ans


def rec(s):
    """recursive solution
    """
    if len(s) <= 1:
        return s
    return rec(s[1:]) + s[0]


# tests

assert "meesa" == sol1("aseem")
assert "meesa" == sol2("aseem")
assert "meesa" == sol3("aseem")
assert "meesa" == sol4("aseem")
assert "meesa" == sol5("aseem")
assert "meesa" == sol6("aseem")
assert "meesa" == rec("aseem")
assert "!evitacudE ot emocleW" == sol1("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol2("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol3("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol4("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol5("Welcome to Educative!")
assert "!evitacudE ot emocleW" == sol6("Welcome to Educative!")
