# Objective is to use multi return from method just like Go lang
# return could be accepted in the tuple
# Important: any data type can be return, there is no enforcement what should be returned.
# If nothing is returned, None is returned by default.

# @Author Aseem Jain


def multi_return(arg=2):
    if arg is 1:
        return "A"
    if arg is 2:
        return 10, 2
    if arg is 3:
        return "10, a2"
    if arg is 4:
        return ["a","b","c"]

(num1, num2) = multi_return()
nums = multi_return()

# print(" number1 is ", num1)
# print(" number1 is ", num1)
# print(" number2 is ", nums)

## output
# number1 is 10
# number1 is 10
# number2 is (10, 2)
print(multi_return(1))
print(multi_return(2))
print(multi_return(3))


