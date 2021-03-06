# Find out if string is not blank or None

#####################################
""" Utility Function """
#####################################
# Returns the max/min value from args or iterable
# With a single iterable argument, return its biggest item.

total = 125
current = 15
my_max = max(total, current)
my_min = min(total, current)

l = [1, 4, 7, 43, 23, 89, 2]
s = set([1, 4, 7, 43, 23, 89, 2])

my_max = max(l)
my_max = max(s)

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
print(str.strip('0'))

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
# find char in word, can also specify length range returns -1 if not found, else index

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
# convert num to char and char to number
ord('a')
# >>> 97
chr(97)
# >>> 'a'
chr(ord('a') + 3)
# >>> 'd'

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
""" Random generation or picking """
#####################################
import random

random.random()
# will print random number between 0 and 1
# >> 0.45432223345433

random.randint(0,10)
# will print random number between 0 and 10 ie given range
# >> 0.45432223345433

random.choice(["aseem","atul","sunita"])
# will print one element in the given list randomly
# >> sunita

#####################################
""" Variable assignments """
#####################################
# Swap the variable:
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# Ternary assignment:
max = a if a > b else b

# swap variable without temp
a, b = b, a

# (get_this_if_false, get_this_if_true)[condition]
age = 20
can_vote = ("no", "yes")[age > 18]
can_vote = "yes" if age > 18 else "no"
print("can vote {} ? {}".format(age, can_vote))

# toggle or flip flop or ternary operator
e = "enter"
toggle = "flop" if e == "flip" else "flip"

# flip the boolean var
flip = True
flip = not flip

#####################################
""" Printing tricks """
#####################################
# print on same line
print("aseem", end=" ")
print("jain")

# print a horizontal line by multiplication
print("-" * 40)

# print in aligned way with with expandtabs
print("{}:  \t  {} ".format(a, b).expandtabs(50))
print("do it aligned{}:  \t  {} ".format(a, b).expandtabs(50))

#####################################
""" FUNCTIONS """
#####################################
# Function argument unpacking

def myfunc(x, y, z):
    print(x, y, z)

tuple_vec = (1, 0, 1)
dict_vec = {'x': 1, 'y': 0, 'z': 1}

myfunc(*tuple_vec)
# >> 1, 0, 1

myfunc(**dict_vec)
# >> 1, 0, 1


#####################################
""" ARRAYS  LISTS """
#####################################
# Figure out if list is not empty

a = []
if not a:
    print("List is empty")
else:
    print("do your stuff")

#####################################
# looping over empty list

lst = [1, 2, 3, 4]
lst2 = [1, 2, 3, 4, 6]

# Old school (direct access instead of iterating)
for i in range(0, len(lst), 1):
    print(lst[i])

# Iteration to get value without index
for ele in lst:
    print(ele)

# Iteration with index and value both, can start with 1
for index, ele in enumerate(lst, start=1):
    print(index, ele)

# Iterating multiple lists or enumerable objects together, runs to shorted of 2
for e1, e2 in zip(lst, lst2):
    print(e1, e2)

# while and for loop evaluate to false if list is empty or none and does throw error
itr = iter(lst)
cnt = 0
while cnt < len(lst):
    cnt += 1
    try:
        print(next(itr))
    except StopIteration:
        pass
else:
    print("print this if loop is not broken")

#####################################
# List comprehension : convert num list into string list

arr = [3, 4, 5, 4, 3, 2]
arrs = [str(x) for x in arr]

# normal
l = [x for x in range(100)]

# if
lc_if = [x for x in l if x >= 45]

# if / else
lc_if_else = [x + 1 if x >= 45 else x + 5 for x in l]

#####################################
# Removing item from list
list = [2, 3, 4, 0, 1, 8]

# Remove an item by value: remove()
list.remove(0)

# Remove an item by index and get its value (defaults to last or -1): pop()
list.pop()
list.pop(2)

# Remove items by index or slice: del
del list[2]
del list[2:4]

# Remove items that meet the condition: List comprehensions
list = [e for e in list if e % 2 == 0]

# Remove all items: clear()
l.clear()

#####################################
# combining or extending another list
# Will add all elements of b in a maintaining the order.

a = [1, 2, 3, 4]
b = [9, 6, 5, 4]
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
# get a random element from a list
import random
given_list = [1,2,3,4,5]
random.choice(given_list)

#####################################

# Generate list with similar items, create list with 5 false elements
visited = [False] * 5

#####################################
# Create new sorted list

a = [5, 4, 3, 7, 8, 45]
new_a = sorted(a, reverse=True)

#####################################
# Compare 2 lists are equal
a = [5, 4, 3, 7, 8, 45]
b = [4, 5, 3, 7, 45, 8]
sorted(a) == sorted(b)

#####################################
# Find union in 2 lists
union = a.copy()
union.extend(b)

# list looping
union = a.copy()
for x in b:
    union.append(x)

#####################################
# Find intersection in 2 lists

set(a).intersection(b)

# list compherension
[x for x in a if x in b]

#####################################
# Find unique in 2 lists

set(a).intersection(b)

# list compherension
[x for x in a if x in b]

#####################################
# Find unique or uncommon  in 2 lists ( difference)

diff = []
for x in a:
    if x not in b and x not in diff:
        diff.append(x)

for x in b:
    if x not in a and x not in diff:
        diff.append(x)

# convert list into set and do difference or minus operator
diff = a.difference(b)
diff = a - b


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

# sort custom object
# 1. Static way : class implementing < less then __lt__(self,other)
# 2. Dynamic way is by providing lambda func with key.

class Custom():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + " " + self.age

    def __lt__(self, other):
        return self.age < other.age


# obj = Custom("aseem", "jain")
custom_array = [Custom("aseem", "jain"), Custom("wseem", "jain"), Custom("nehal", "zain")]
# custom_array=[]
print(custom_array)
custom_array.sort()
custom_array.sort(key=lambda x: x.name, reverse=True)
print(custom_array)
custom_array.sort(key=lambda x: x.age, reverse=True)
print(custom_array)


#####################################
# sort list of date strings as date by parsing
from datetime import datetime

my_dates = ['5-Nov-18', '25-Mar-17', '1-Nov-18', '7-Mar-17']
my_dates.sort(key=lambda x: datetime.strptime(x, "%d-%b-%y"))

# sorting list of map with dates
coupons =[ {"Category Name":"Dhoom1",  "Modified date": "2018-11-20"},
           {"Category Name":"Dhoom2",  "Modified date": "2018-11-10"} ]
coupons.sort(key=lambda x: datetime.strptime(x["Modified date"], "%Y-%m-%d"))

#####################################
# Type hint in methods
#####################################
# func takes 2 args of type int and str and returns str

def sub_this(x: int, obj:Custom) -> str:
    return f'{obj.name} is {x} year old'

# by using typing, define the element type / generics and get auto completion
from typing import List
mylist: List[Custom] = []

#####################################
""" Dictionaries or Maps"""
#####################################


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
# elements must be immutable in set
# list/Map or unhashable or object reference cannot be added in set, but class object can
# It is also built in the same way as dict, where key and value is same.
#####################################

# create set in 2 ways, argument to set() is an iterable
set1 = set()
set2 = {3, 6, 9, 12, 15}

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
set1.update([3, 4, ], [7, 8])

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

# Delta - difference or uncommon or unique elements
set1 - set2  # elements of set1 - set2
set2 - set1  # elements of set1 - set2
set1.difference(set2)

# Immutable set or Frozen set, cannot add or updated / ENUM
froze_set = frozenset([1, 2, 3, ])

#####################################
""" MAP or DICTIONARY   """
# set  has no duplicates.
# set is unordered.
# It is also built in the same way as dict, where key and value is same.
#####################################

# creating map
m = {"a": 1}

# adding
m["key"] = "value"

# Retrieve value by key, through error if key not found
m["key"]

# Returns None if key does not exists
m.get("key")

# Return value if key presents, set default if key is not present.
m.setdefault("key", "default")

d = {}
lst = d.setdefault("key",[])
lst.append(0)

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
for k, v in m.items(): print(k, v)

# update map , update existing keys and adds new keys
d1 = {'a': 10, 'b': 20, 'c': 30}
d1.update(b=200, d=400)
# d1 => {'a': 10, 'b': 200, 'c': 30, 'd': 400}

# Merge dictionary with update
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'b': 200, 'd': 400}
# merged in existing
d1.update(d2)

# create new dict with unpacking
merged_dict = {**d1, **d2}

# d1 => {'a': 10, 'b': 200, 'c': 30, 'd': 400}



#### Sorting dictionary or map by Values ########
# Sorting by dict comprehension
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
{k: v for k, v in sorted(x.items(), key=lambda item: item[1])}
# out=> {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}


# convert dict tuples and sort them by key or value using lambda
s_k_t = sorted(m.items(),key=lambda i:i[0])
s_v_t = sorted(m.items(),key=lambda i:i[1])

# Converted tuple into map by
## dict(s_k_t)
dict(s_k_t)

dict(sorted(x.items(), key=lambda item: item[1]))
# out=> {0: 0, 2: 1, 1: 2, 4: 3, 3: 4}

## Iterate to convert
s_k_m = {}
for k,v in s_k_t:
    s_k_m[k]=v

##### Deep clone a map by using dictionary compehension

# manual copy at first level
deep_copied_map = { k:v.copy() for k,v in map.items() }

# in build method
import copy
deep_copied_map = copy.deepcopy(s_k_m)


#####################################
""" Using default dictionary for data crunching from list /tuples  
d = defaultdict(<datatype>)
Instead of giving key missing error, it would set default key with default value of given datatype 
Using the Python defaultdict Type for Handling Missing Keys and doing
1. Grouping Items
2. Grouping Unique Items
3. Counting Items
4. Accumulating Values or Aggregation
"""
#####################################
from collections import defaultdict

# 1. Grouping Items
m = defaultdict(list)
for k,v in l:
    m[k].append(v)

# 2. Grouping Unique Items
m = defaultdict(set)
for k,v in l:
    m[k].add(v)

# 3. Counting Items
m = defaultdict(int)
for k, _ in l:
    m[k] += 1

# 4. Accumulating Values or Aggregation
m = defaultdict(float)
for k,v in l:
    m[k] += v

#####################################
""" Data driven Testing   """
#####################################

def sol(n):
    return n*2

test_data = [
    (2 ,4),
    (4 ,8),
]

for given, expected in test_data:
    assert expected == sol(given)
    print(f"Test passed for: given {given} and expected = {expected}")


#####################################
""" pytest Testing    """
#####################################
import pytest

# Run test by keyword or substring in test name
# $ pytest -k great -v

# Mark test to run
#@pytest.mark.<markername>

# $ pytest -m <markername> -v
@pytest.mark.sqr
def test_sqr():
    num = 25
    assert 5 * 5 == num
# $ pytest -m sqr -v

####################################
# Data driven testing with all combination of inputs
@pytest.mark.parametrize("num, output",[(1,11),(2,22),(3,35),(4,44)])
def test_multiplication_11(num, output):
    assert 11 * num == output

####################################
# Setup and Tear down fixtures
@pytest.fixture()
def data_service():
    print("setup objexts")
    yield [1,2,3,4]
    print("clean up date")

def test_sum(data_service):
    assert 10 == sum(data_service)


####################################
# skip a test by annotation
@pytest.mark.skip
def test_flaky():
    pass

####################################
# run tests with report
# $ coverage report test_simple.py
# Name             Stmts   Miss  Cover
# ------------------------------------
# test_simple.py      11      1    91%
# ------------------------------------
# TOTAL               11      1    91%

####################################

# run test with code coverage in html
# $ coverage html test_simple.py

# open html converage file
# open htmlcov/index.html
