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

#####################################
# convert string in list of chars
s = "aseem jain"
sa = list(s)
set = set(s)
print(sa,set)

#####################################
# check if char or string contains special chars, is numeric, is a negative number or alphabetic

# String does not have special chars including space
"aseem456".isalnum()

# Find out string is only alphabetic
"aseem".isalpha()

# Find string is digit or numeric, ( does not check negative numbers)
"456".isnumeric()

# Find string is negative number.
num = "-486"
def is_num(num):
    try:
        int(num)
        return True
    except:
        return False

#####################################
# Populate a matrix

input = ["YYNN","YYYN","NYYN","NNNY"]
m = []
for e in a:
    m.append(list(e))

    # ['Y', 'Y', 'N', 'N']
    # ['Y', 'Y', 'Y', 'N']
    # ['N', 'Y', 'Y', 'N']
    # ['N', 'N', 'N', 'Y']

#####################################