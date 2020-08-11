# Find out if string is not blank or None

#####################################
""" Utility Function """
#####################################
# Returns the max/min value from args or iterable
# With a single iterable argument, return its biggest item.

total =125
current = 15
my_max = max(total, current)
my_min = min(total, current)

l = [1,4,7,43,23,89,2]
s = set(1,4,7,43,23,89,2)

my_max =  max(l)
my_max =  max(s)


#####################################
""" String Operations """
#####################################

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
stri = "+".join(arr)
print(stri)
#####################################

# Count: Return the number of non-overlapping occurrences of substring
print("aseem".count("e"))
#####################################
# find char in word, can also specify length range returns -1 if not find, else index

"aseem".find("s")
print("aseem jain".find("m", 0, 5))
#####################################

# Replace: Return a copy with all occurrences of substring old replaced by new.
print("aseem".replace("e", "x"))

#####################################
# convert string in list of chars
s = "aseem jain"
sa = list(s)
set = set(s)
print(sa, set)

#####################################
# Reverse a String using slice

a = "aseem jain"
a = a[::-1]
a = "".join(list(reversed(a)))
print(a)

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

# String template for interpolation
from string import Template
GET_USER_ENDPOINT = Template("$API_ENDPOINT/v2.0/users/$USER_ID")
final_string = GET_USER_ENDPOINT.substitute(API_ENDPOINT="localhost", USER_ID=786231)

#####################################
""" Variable assignments """
#####################################
# Swap the variable:
a,b=10,20
print(a,b)
a, b = b, a
print(a,b)

# Ternary assignment:
max = a if a > b else b


# (get_this_if_false, get_this_if_true)[condition]
age = 20
can_vote = ("no","yes")[age > 18]
print("can vote {} ? {}".format(age, can_vote))

#####################################
""" Printing tricks """
#####################################
# print on same line
print("aseem", end=" ")
print("jain")

# print a horizontal line by multiplication
print("-"*40)

# print in aligned way with with expandtabs
print("{}:  \t  {} ".format(a,b).expandtabs(50))
print("do it aligned{}:  \t  {} ".format(a, b).expandtabs(50))

#####################################
""" ARRAYS  LISTS """
#####################################
#####################################
# Figure out if list is not empty

a=[]
if not a:
  print("List is empty")
else:
  print("do your stuff")


#####################################
# Create new sorted list

a=[5,4,3,7,8,45]
new_a = sorted(a, reverse=True)


#####################################
# Reverse array without sorting using the slice function

arr = [1, 2, 5, 7, 5, 4, 3, 1]
rev_arr = arr[::-1]

#####################################
# sort array in place in reverse order

arr = [1, 2, 5, 7, 5, 4, 3, 1]
arr.sort(reverse=True)

#####################################

# sort custom object by key
class Custom():
    def __init__(self,fn,ln):
        self.fn = fn
        self.ln = ln
    def __repr__(self):
        return self.fn + " " + self.ln

# obj = Custom("aseem", "jain")
custom_array = [Custom("aseem", "jain"),Custom("wseem", "jain"),Custom("nehal", "zain") ]
# custom_array=[]
print(custom_array)

custom_array.sort(key=lambda x: x.fn, reverse=True)
print(custom_array)
custom_array.sort(key=lambda x: x.ln, reverse=True)
print(custom_array)
#####################################
# List comprehension : convert num list into string list

arr = [3,4,5,4,3,2]
arrs = [str(x) for x in arr]
print(arr)

#####################################
""" MATRIX  """
#####################################
# Populate a matrix

input = ["YYNN", "YYYN", "NYYN", "NNNY"]
m = []
for e in input:
    m.append(list(e))

    # ['Y', 'Y', 'N', 'N']
    # ['Y', 'Y', 'Y', 'N']
    # ['N', 'Y', 'Y', 'N']
    # ['N', 'N', 'N', 'Y']

#####################################
