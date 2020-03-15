# Pranagrams are Sentences which contains all alphabets from a to z.
# The sentence "A quick brown fox jumps over the lazy dog" contains every single letter in the alphabet.
# Such sentences are called pangrams.
# You are to write a method getMissingLetters, which takes a String, sentence, and returns all the letters it is missing (which prevent it from being a pangram).
# You should ignore the case of the letters in sentence, and your return should be all lower case letters, in alphabetical order.

def getMissingLetters(s):
    base = 'abcdefghijklmnopqrstuvwxyz'
    base_set = set(base)
    s = set(s.lower())
    diff = list(base_set.difference(s))
    diff.sort()
    ans = "".join(diff)
    print(ans)
    return ans
i1 =  "A quick brown fox jumps over the lazy dog"
i2 =  "A quick brown fox jumps over the dog"
i3 =  "A quick brown fox jumps over the lafy dog"

assert getMissingLetters(i1) is ""
assert getMissingLetters(i3) == "z"
assert getMissingLetters(i2) == "lyz"
