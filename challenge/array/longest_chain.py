# String Chains
# Given an array of words representing your dictionary, you test each word and see if it can be made into another word in the dictionary.
# This will be done by removing characters one at a time.  Each word represents its own first element of its string chain,
# so start with a string chain length of 1.  Each time you remove a character, increment your string chain by 1.
# In order to remove a character, the resulting word must be in your original dictionary.
# Your goal is to determine the longest string chain achievable for a given dictionary.
# For example, given a dictionary [a, and, an, bear], the word and could be reduced to an and then to a.
# The single character a cannot be reduced any further as the null string is not in the dictionary.
# This would be the longest string chain, having a length 3.  The word bear cannot be reduced at all.
# Function Description:
# Complete the function longestChain in the editor below.
# The function must return a single integer representing the length of the longest string chain.
# longestChain has the following parameter(s):
#   words[words[0],…words[n-1]]: an array of strings to test
# Constraints:
# 1 <= n <= 50000
# 1 <= |words[i]| <= 60, where 0 <= I < n
# Each words[i] is composed of lowercase letters in asci[a-z]

### Algorithm:
# sort dict in length
# try the biggest string and reduce 1 char at a time and see if it exists untill it reduces to 1 char


d = ["a", "and", "an", "bear", "asdfasdfasffe", "ear", "bee","hoping", "guruji","c","guruj","guru","gur","gu","g"]
d.sort(key=lambda x:len(x),reverse=True)
print(d)

def longest_chain(d):
    max_len = 1
    for w in d:
        c_l = len(w)
        cand = True
        for i in range(1,c_l):
            if(w[:c_l-i] not in d):
                cand=False
                break
        if cand:
            return c_l

    return max_len


assert longest_chain(d) is 6

