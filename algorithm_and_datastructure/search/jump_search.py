# Jump Search
# find if element is in the sorted list
"""
Jump Search
With Jump Search, the sorted array of data is split into subsets of elements called blocks. We find the search key (input value) by comparing the search candidate in each block. As the array is sorted, the search candidate is the highest value of a block.

When comparing the search key to a search candidate, the algorithm can then do 1 of 3 things:

If the search candidate is lesser than the search key, we'll check the subsequent block
If the search candidate is greater than the search key, we'll do a linear search on the current block
If the search candidate is the same as the search key, return the candidate
The size of the block is chosen as the square root of the array's length. Therefore, arrays with length n have a block size of √n, as this on average gives the best performance for most arrays.
"""
import math
lst = [1, 3, 4, 5, 7, 8, 32,35,50,60,70,75,80]

# slide the window un till number less then last element
# iterate each element in last window

#element
e = -80

# window size
ws = int(math.sqrt(len(lst)))
for i in range(0,len(lst),ws):
    if e == lst[i]:
        print("found")
        break
    if e > lst[i]:
        continue

    for j in range(i,i-ws,-1):
        if e == lst[j]:
            print("found")
            break
    else:
        print("not found")
        break
else:
    print("not found")



