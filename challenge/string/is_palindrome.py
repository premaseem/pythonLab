# A palindrome is a word, number, phrase, or any other sequence of characters that reads the same forward as it does backward.

def is_palindrome_sol1(s):
    s = s.lower().replace(" ","")
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


def is_palindrome_sol2(s):
    i = 0
    j = len(s) - 1

    while i < j:
        # ignore white space
        while not s[i].isalnum() and i < j:
            i += 1
        while not s[j].isalnum() and i < j:
            j -= 1

        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

assert is_palindrome_sol1("Was it a cat I saw")
assert is_palindrome_sol2("Was it a cat I saw")