# You are to write a program that takes a list of strings containing integers and words and returns a sorted version of the list.
# The goal is to sort this list in such a way that all words are in alphabetical order and all integers are in numerical order.
# Furthermore, if the nth element in the list is an integer it must remain an integer, and if it is a word it must remain a word.
# Input:
# The input will contain a single, possibly empty, line containing a space-separated list of strings to be sorted. Words will not contain spaces, will contain only the lower-case letters a-z. Integers will be in the range -999999 to 999999, inclusive. The line will be at most 1000 characters long.
# Output:
# The program must output the list of strings, sorted per the requirements above. Strings must be separated by a single space, with no leading space at the beginning of the line or trailing space at the end of the line.
# Constraints:
# The code you submit must take input from stdin and produce output to stdout as specified above. No other output is permitted. You can assume the input will be valid. Feel free to use standard libraries to assist in sorting.
#
# Example 1:
# Input:
# 1
# Output:
# 1
#
# Example 2:
# Input:
# car truck bus
# Output:
# bus car truck
#
# Example 3:
# Input:
# 8 4 6 1 -2 9 5
# Output:
# -2 1 4 5 6 8 9
#
# Example 4:
# Input:
# car truck 8 4 bus 6 1
# Output:
# bus car 1 4 truck 6 8


# Algorithm:
# separate int and string array
# sort them and put again back based on index
i1 = "car truck 8 4 bus 6 1"
def sort_string(input):
    arr = input.split(" ")
    da=[]
    sa=[]
    for e in arr:
        if not e.isalpha():
            da.append(int(e))
        else:
            sa.append(e)
    da.sort()
    sa.sort()
    sai = 0
    dai = 0
    for i, e in enumerate(arr):
        if not e.isalpha():
            arr[i] = str(da[dai])
            dai += 1
        else:
            arr[i] = sa[sai]
            sai += 1
    return " ".join(arr)

# Test cases
test_cases = [
            ("1","1"),
           ("car truck bus", "bus car truck"),
           ("8 4 6 1 -2 9 5", "-2 1 4 5 6 8 9"),
           ("car truck 8 4 bus 6 1", "bus car 1 4 truck 6 8")
    ]

for test_data in test_cases:
    print(" Testing input: {} \t actual: {} \t expected: {} ".format(test_data[0], sort_string(test_data[0]), test_data[1]).expandtabs(50))
    assert sort_string(test_data[0]) == test_data[1]