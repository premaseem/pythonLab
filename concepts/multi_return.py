# Objective is to use multi return from method just like Go lang
# return could be accepted in the tuple
# @Author Aseem Jain


def multi_return():
    return 10, 2

(num1, num2) = multi_return()
nums = multi_return()

print(" number1 is ", num1)
print(" number1 is ", num1)
print(" number2 is ", nums)

## output
# number1 is 10
# number1 is 10
# number2 is (10, 2)
