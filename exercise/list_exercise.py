# Question 1: Given the list below, print the min value from the list using the
# min function
my_list = [903,373,223,4031,2033,535,677,601,403,340,370,352,441,293,567,8888,1031,788,161]
## Write your code below, 1 line
print("min value is ", min(my_list))
# End question 1

# Question 2: Given the list below, using the 'in' operator, print (True or False) if
# 'urgent' exists in the list.
my_words_list = ['extreme', 'arrow', 'urgently', 'important', 'Urgent', 'imperative']
## Write your code below, 1 line
print("print (True or False)-> ", 'urgently' in my_words_list)
# End question 2

# Question 3: Use the sorted function to sort my_list from question 1 and assign it to a variable
# named my_sorted_list
## Write your code below, 1 line
my_sorted_list = sorted(my_list)
# End question 3

# Question 4: Use the sort method to sort my_list from above and print out my_list below it
## Write your code below, 2 lines
my_list.sort()
print(my_list)

# End question 4

# Question 5: Use the equality test to check if my_sorted_list is equal to my_list. Remember
# to print the result.
## Write your code below, 1 line
print("Are both equal ",my_sorted_list == my_list)
# End question 5

# =================

# Question 1: Given the two lists below, add all the elements in the second list
# to the end of the first list, then print out the first list. Choose the
# appropriate method to add these elements so that you don't end up with a list
# within a list (as in the first list 'my_courses' should only have string data,
# not lists of strings).
my_courses = ['comp sci','economics','physics','astronomy']
new_courses = ['climate studies','artificial intelligence']
## Write your code below, 2 lines ##
my_courses.extend(new_courses)

## End question 1

# Question 2: Given the string below, add it to the end of my_courses list which
# you printed at the end of question 1, then print out my_courses
new_course = 'tennis'
## Write your code below, 2 lines
my_courses.append(new_course)

# End question 2

# Question 3: Choose the approprite method to delete 'economics' from my_courses
# list and print the resulting my_courses list.
## Write your code below, 2 lines
my_courses.remove('economics')
print(my_courses)

# End question 3

# Question 4: Given the integer list below, print the length of the list (number
# of integers in the list).
my_int_list = [9,6,13,7,27,99,104,100,10,16,42,64]
## Write your code below, 1 line
len(my_int_list)
# End question 4

# Question 5: Grab the second half of my_int_list using slice notation and print
# it to the screen
## Write your code below, 1 line
print(my_int_list[len(my_int_list)//2:])
print(my_int_list)
# End question 5