
s = "I am a good man"

def cnt(s):
    if not s:
        return 0
    return 1 + cnt(s[1:])

print(cnt(s))