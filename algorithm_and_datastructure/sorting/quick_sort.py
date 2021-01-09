"""
Returns sorted list of integers using Quicksort
Input: Unsorted list of integers
Note: This is not an in-place implementation
"""

l = [10, 9, 4, 7, 2, 4]
# l = [1,2,3,4,5]
e = [2, 4, 4, 7, 9, 10]


def quick_sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return quick_sort(less)+equal+quick_sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

l = quick_sort(l)
print("Is sorted properly", e == l)
