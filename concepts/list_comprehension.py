# Objective: Remove elements present in other list  using list comprehension
# @Author Aseem Jain


# initializing list
test_list = [1, 3, 4, 6, 7]

# initializing remove list
remove_list = [3, 6]

# printing original list
print("The original list is : " + str(test_list))

# printing remove list
print("The original list is : " + str(remove_list))

# using list comprehension to perform task
res = [i for i in test_list if i not in remove_list]

# printing result
print("The list after performing remove operation is : " + str(res))