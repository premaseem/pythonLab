# how to convert the column IDs in a spreadsheet into an integer in Python
# we will be considering how to solve the problem of implementing a function that converts a spreadsheet column ID (i.e., “A”, “B”, “C”, …, “Z”, “AA”, etc.) to the corresponding integer. For example, “A” equals 1 because it represents the first column, while “AA” equals 27 because it represents the 27th column.

# Spread sheet base 26 numbers encoding

def get_val(c):
    v  = ord(c) - ord('A') + 1
    return v

def spreadsheet_encode_column_sol1(s):
    p = 0
    f = 0
    s = list(s)
    while s:
        v = get_val(s.pop())
        f = f + (26 ** p) * v
        p += 1
    return f

def spreadsheet_encode_column_sol2(col_str):
    num = 0
    count = len(col_str)-1
    for s in col_str:
        num += 26**count * (ord(s) - ord('A') + 1)
        count -= 1
    return num

assert 1 == get_val("A")
assert 27 == spreadsheet_encode_column_sol1("AA")
assert 27 == spreadsheet_encode_column_sol2("AA")