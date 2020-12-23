############################
"""This algorithm segments the list into two parts: sorted and unsorted.
We continuously remove the smallest element of the unsorted segment of the list and append it to the sorted segment"""
############################

def selection_sort(nums):
    # This value of i corresponds to how many values were sorted
    for i in range(len(nums)):
        # We assume that the first item of the unsorted segment is the smallest
        lowest_value_index = i
        # This loop iterates over the unsorted items
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        # Swap values of the lowest unsorted element with the first unsorted
        # element
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


# Verify it works
random_list_of_nums = [12, 8, 3, 20, 11]
selection_sort(random_list_of_nums)
print(random_list_of_nums)

############################
# with for loop and continuous swaping
############################
l = [10,9,4,7,2,4]
# l = [1,2,3,4,5]
e = [2,4,4,7,9,10]


for x in range(len(l)):
    print(f"running for position {x} :{l}")
    for y in range(x,len(l)):
        if l[x] > l[y]:
            l[x], l[y] = l[y], l[x]

print("Is sorted properly", e == l, l)

############################
# with While loop and continuous swaping
############################

l = [10,9,4,7,2,4]
# l = [1,2,3,4,5,6]
e = [2,4,4,7,9,10]

hits = 1
spot_marker = 0
while spot_marker < len(l):
    print(f"running for spot marker {spot_marker} :{l}")
    hits += 1
    for i in range(spot_marker, len(l)):
        hits += 1
        if l[spot_marker] > l[i]:
            l[spot_marker],l[i] = l[i] , l[spot_marker]

    spot_marker += 1

print("Is sorted properly ",hits, e == l, l)