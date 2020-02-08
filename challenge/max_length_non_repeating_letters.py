
# "nndfddf" len is 3


def get_max_len(s):
    max = 1
    cnt = 0
    for i in range(1,len(s)):

        if s[i] == s[i-1]:
            cnt = 0
        else:
            cnt += 1

        if max < cnt:
            max = cnt

    return max


assert 3 == get_max_len("nndfddf")
assert 5 == get_max_len("aseemjain")
