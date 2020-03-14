# Find the number of occurrence of letter in a word
# sample output: r 1 a 2 s 1 p 1 e 1 k 1 c 2
i1 = "Rackspace"
i2 = "Aseem Jain ia a good boy"

for c in set(i1.lower()):
    print(c, i1.lower().count(c), end=" ")