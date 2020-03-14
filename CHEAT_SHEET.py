# Find out if string is not blank or None

myString = None
myString = ""

if not myString:
    print("invalid string")

#####################################
# Remove white space from back and front of string

myString = "    aseem    jain   "
a = myString.strip(" ")
print(a)
#####################################

# Split: Return a list of the words in the string, using sep as the delimiter string.
arr = "to-do-is-nice".split("-")
print(arr)
#####################################

# Join: The string whose method is called is inserted in between each given string.
str = "+".join(arr)
print(str)
#####################################

# Count: Return the number of non-overlapping occurrences of substring
print("aseem".count("e"))
#####################################
# find char in word, can also specify length range returns -1 if not find, else index

"aseem".find("s")
print("aseem jain".find("m",0,5))
#####################################

# Replace: Return a copy with all occurrences of substring old replaced by new.
print("aseem".replace("e","x"))


