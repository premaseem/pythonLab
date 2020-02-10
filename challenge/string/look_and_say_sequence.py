# Write code to generate next number of look and say sequence
# 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...

# Description
# To generate a member of the sequence from the previous member, read off the digits of the previous member and record the count of the number of digits in groups of the same digit.
#
# For example, 1 is read off as one 1 which implies that the count of 1 is one. As 1 is read off as “one 1”, the next sequence will be written as 11 where 1 replaces one. Now 11 is read off as “two 1s” as the count of “1” is two in this term. Hence, the next term in the sequence becomes 21.

def gen(num):
    if num == "1":
        return "11"
    fa = []
    cnt = ""
    save_last = True
    for i in range(0, len(str(num)) - 1):
        if num[i] == num[i + 1]:
            cnt = cnt + str(num[i])
            if (i + 1 != len(str(num)) - 1):
                continue
            else:
                save_last = False

        cnt += str(num[i])
        fa.append(cnt)
        cnt = ""
    if save_last:
        fa.append(num[-1])

    # print(fa)
    s = ""
    for item in fa:
        v = str(len(item)) + str(item[-1])
        s = s + v
    return s


assert "1113213211" == gen("13112221")

# generate first 5 number in sequence
input = "1"
for i in range(10):
    print(i + 1, input)
    input = gen(input)

# Sample out of sequence
# /Users/asejain/virtualEnvironment/python3/bin/python /Users/asejain/PycharmProjects/pythonPlayground/challenge/string/look_and_say_sequence.py
# 1 1
# 2 11
# 3 21
# 4 1211
# 5 111221
# 6 312211
# 7 13112221
# 8 1113213211
# 9 31131211131221
# 10 13211311123113112211
