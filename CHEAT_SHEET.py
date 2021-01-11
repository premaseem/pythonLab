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
# Remove white space or given char  from back and front of string

myString = "    aseem    jain   "
a = myString.strip(" ")

myString = "0000000this is string example....wow!!!0000000";
print (str.strip( '0' ))

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

# slicing with step function and reassigning back
a = a[::-1]

# convert in list, reverse it and join back
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

# swap variable without temp
a, b = b, a


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
# looping over empty list

# while and for loop evaluate to false if list is empty or none and does throw error
while a:
    print(a)

for i in a:
    print(a)

#####################################
# List comprehension : convert num list into string list

arr = [3,4,5,4,3,2]
arrs = [str(x) for x in arr]

# normal
l = [x for x in range(100)]

# if
lc_if = [x+1 if x >= 45 else x+5 for x in l]

# if / else
lc_if_else = [x+1 if x >= 45 else x+5 for x in l]


#####################################
# Removing item from list
list = [2,3,4,0,1,8]

# Remove an item by value: remove()
list.remove(0)

# Remove an item by index and get its value (defaults to last or -1): pop()
list.pop()
list.pop(2)

# Remove items by index or slice: del
del list[2]
del list [2:4]

# Remove items that meet the condition: List comprehensions
list = [e for e in list if e % 2 == 0 ]


# Remove all items: clear()
l.clear()


#####################################
# combining or extending another list
# Will add all elements of b in a maintaining the order.

a = [1,2,3,4]
b = [9,6,5,4]
a.extend(b)

# creating 3rd array by adding 2 arrays
c = a + b

# a = [1, 2, 3, 4, 9, 6, 5, 4]
#####################################

# Create type safe or homogenious lists, will only add integer type

import array

integer_array = array.array('i', [10, 11, 12, 12, 13])

# Find index of value
vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# index of 'e' in vowels
index = vowels.index('e')
print('The index of e:', index)

#####################################

# Generate list with similar items, create list with 5 false elements
visited = [False] * 5


#####################################
# Create new sorted list

a=[5,4,3,7,8,45]
new_a = sorted(a, reverse=True)


#####################################
# Reverse array without sorting using the slice function

arr = [1, 2, 5, 7, 5, 4, 3, 1]

# reverse with slicing and step function, reassign to new obj
rev_arr = arr[::-1]

# in place reverse the arr without sorting.
arr.reverse()

# in place reverse the arr with sorting.
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
""" SET operation  """
# set  has no duplicates.
# set is unordered.
# elemets must be immutable in set
# It is also built in the same way as dict, where key and value is same.
#####################################

# create set in 2 ways, argument to set() is an iterable
set1 = set()
set2 = {3,6,9,12,15}

# add element
set1.add(2)
set1.add(2)
set1.add(4)
set1.add(6)
set1.add(8)
set1.add(10)

# search element - key in container
if 2 in set1:
    print("found key")

# remove element
set1.remove(8)

# remove element without error if element not found
set1.discard(8)

# extends or add elements in set, argument is iterable
set1.update([3,4,], [7,8])

# Intersection - common elements
set1 & set2
set1.intersection(set2)

# Union - combined
set1 | set2
set1.union(set2)

# is subset
set1 <= set2
set1.issubset(set2)

# is superset
set1 >= set2
set1.issuperset(set2)

# sets equality operation
set1 == set2

# Delta - difference or uncommon elements
set1 - set2 # elements of set1 - set2
set2 - set1 # elements of set1 - set2
set1.difference(set2)

# Immutable set or Frozen set, cannot add or updated / ENUM
froze_set = frozenset([1,2,3,])


#####################################
""" MAP or DICTIONARY   """
# set  has no duplicates.
# set is unordered.
# It is also built in the same way as dict, where key and value is same.
#####################################

# creating map
m = {"a":1}

# adding
m["key"] = "value"

# Retrieve value by key, through error if key not found
m["key"]

# Returns None if key does not exists
m.get("key")

# Return value if key presents, set default if key is not present.
m.setdefault("key", "default")

# deleting key
m.pop("key")
del m["key"]

# Searching for key
if "key" in m:
    print("found")

# iterating keys, by default m refers to m.keys()
for k in m: print(k)
for k in m.keys(): print(k)

# iterate values
for k in m.values(): print(k)

# iterate items as key and value
for k in m.items(): print(k)

# iterate and unpack keys and values
for k,v in m.items(): print(k,v)

# update map , update existing keys and adds new keys
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
# d1 => {'a': 10, 'b': 200, 'c': 30, 'd': 400}

# Merge dictionary with update
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
# d1 => {'a': 10, 'b': 200, 'c': 30, 'd': 400}