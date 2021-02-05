"""

@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

Find Symmetric Pairs in a List

Input = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
Output = [[3, 4], [4, 3], [5, 9], [9, 5]]

"""

list = [[1, 2], [3, 4], [5, 9], [4, 3], [9, 5]]
# set(list)
# convert in set
# loop set and find opposite and add in answer list

s = set()
for l in list:
    s.add((l[0],l[1]))
print(s)
ans = []

for e in s:
    compliment = (e[1], e[0])
    if compliment in s:
        ans.append([e[0],e[1]])
print("ans", ans)


############ solution 2 , more optimized

def find_symmetric(my_list):
    # Create an empty set
    pair_set = set()
    result = []
    # Traverse through the given list
    for e in my_list:
        # Make a tuple and a reverse tuple out of the pair
        pair_tup = (e[1], e[0])
        # pair.reverse()
        reverse_tup = (e[0],e[1])
        # Check if the reverse tuple exists in the set
        if(reverse_tup in pair_set):
            # Symmetric pair found
            result.append((e[1], e[0]))
            result.append([e[0],e[1]])
        else:
            # Insert the current tuple into the set
            pair_set.add(pair_tup)
    return result


arr = [[1, 2], [4, 6], [4, 3], [6, 4], [5, 9], [3, 4], [9, 5]]
symmetric = find_symmetric(arr)
print(symmetric)