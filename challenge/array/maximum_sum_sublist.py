"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/
Kadane’s Algorithm

Given an unsorted list AA, the maximum sum sub list is the sub list (contiguous elements) from AA for which the sum of the elements is maximum. In this challenge, we want to find the sum of the maximum sum sub list. This problem is a tricky one because the list might have negative integers in any position, so we have to cater to those negative integers while choosing the continuous sublist with the largest positive values.

"""


def find_max_sum_subarray(lst):
    if (len(lst) < 1):
        return 0;

    curr_max = lst[0];
    global_max = lst[0];
    length_array = len(lst);
    for i in range(1, length_array):
        if curr_max < 0:
            curr_max = lst[i]
        else:
            curr_max += lst[i]
        if global_max < curr_max:
            global_max = curr_max

    return global_max;


lst = [-4, 3,-20,2, -5, 1, 2,-20,100, -3, 25];
print("Sum of largest subarray: ", find_max_sum_subarray(lst));
