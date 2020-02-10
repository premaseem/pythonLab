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



assert "-245" == convert_to_string(-245)