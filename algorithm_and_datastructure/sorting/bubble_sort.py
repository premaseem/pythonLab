#############################
# Bubble sort optimized code
"""We begin by comparing the first two elements of the list. If the first element is larger than the second element, we swap them.
If they are already in order we leave them as is."""
##############################
def bubble_sort(nums):
    # We set swapped to True so the loop looks runs at least once
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                # Swap the elements
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                # Set the flag to True so we'll loop again
                swapped = True


# Verify it works
random_list_of_nums = [5, 2, 1, 8, 4]
bubble_sort(random_list_of_nums)
print(random_list_of_nums)

#########################################
# Bubble sort with while loop

#########################################
# optimized bubble sort to do minimum number of iteration

l = [10,9,4,7,2,4]
# l = [1,2,3,4,5]
e = [2,4,4,7,9,10]

itr = 1
swap_happened = True
while swap_happened:
    swap_happened = False
    print("iternation \t", itr, l)
    itr += 1
    for i in range(len(l) - 1):
        if (l[i] > l[i + 1]):
            l[i], l[i + 1] = l[i + 1], l[i]
            swap_happened = True

print("Is sorted properly", e == l)


