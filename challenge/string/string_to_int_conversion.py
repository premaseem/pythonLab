# convert int into string and back

def convert_to_string(num):
    is_negative = False
    if num < 0:
        is_negative = True
        num = num * -1
    f = ""

    while num > 0:
        r = num % 10
        f = "" + chr(ord('0') +r) + f
        num = num // 10

    if is_negative:
        return "-"+f
    return f

def convert_to_decimal(s):
    is_negative = False
    if s[0] == "-":
        is_negative = True
    s = s[1:]
    s = list(s)
    p = 0
    f = 0
    while s:
        e = s.pop()
        e = ord(e) - ord('0')
        f = f + (10 ** p * e)
        p += 1

    if is_negative:
        return f * -1
    return f


assert "-245" == convert_to_string(-245)
assert -245 == convert_to_decimal("-245")