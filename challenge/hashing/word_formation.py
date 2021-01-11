"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Challenge : Word Formation Using a Hash Table
find whether a given word can be formed by combining two words from a dictionary.

given: lst = ["the", "hello", "there", "answer", "any",
       "by", "world", "their","abc"]

input: word = "helloworld"
output: True
"""

lst = ["the", "hello", "there", "answer", "any",
       "by", "world", "their","abc"]

word = "helloworld"

# Brute Force
for i, w in enumerate(lst):
    for j in range(i+1, len(lst)):
        if w+lst[j] == word:
            print("True")
            break

# Elegent solution
s = set(lst)

for i in range(len(word)):
    p1 = word[:i]
    p2 = word[i:]
    if p1 in s and p2 in s:
        print("True")
        break





