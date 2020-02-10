# an anagram is when two strings can be written using the same letters.
# "William Shakespeare" = "I am a weakish speller"
# "Madam Curie" = "Radium came"

def is_anagram_sol1(s1,s2):
    return sorted(s1.lower().replace(" ",""))== sorted(s2.lower().replace(" ",""))

def is_anagram_sol2(s1,s2):
    # add from first
    d1 = dict()
    for c in s1.lower().replace(" ",""):
        if c in d1:
            d1[c] += 1
        else:
            d1[c] = 1

    # remove from first dict based on second
    for c in s2.lower().replace(" ",""):
        try:
            d1[c] -= 1
        except:
            return False

    for v in d1.values():
        if v > 0:
            return False
    return True

assert is_anagram_sol1("William Shakespeare","I am a weakish speller")
assert is_anagram_sol1("Madam Curie", "Radium came")

assert is_anagram_sol2("William Shakespeare","I am a weakish speller")
assert is_anagram_sol2("Madam Curie", "Radium came")