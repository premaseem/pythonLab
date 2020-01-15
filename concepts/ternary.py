# Objective is to use ternary operator like java
# @Author Aseem Jain

num1, num2 = 10, 12

# traditional
if num1 < num2:
    mymin = num1
else:
    mymin = num2

print(f" {mymin} is min value using tradtional way. ")

# normal ternary
mymin = num1 if num1 < num2 else num2
print(f" {mymin} is min value using normal ternary way. ")

# tuple based ternary (most effective)
mymin = (num2, num1) [num1 < num2]
print(f" {mymin} is min value using tuple based ternary way. ")

# dictionary based
mymin = {True:num1 ,False: num2 } [num1 < num2]
print(f" {mymin} is min value using dictionary based way. ")



