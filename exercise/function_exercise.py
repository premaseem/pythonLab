# Note: We will practice writing simple functions in this exercise to get
# the muscle memory in our fingers going (with typing python functions).

# Question 1: You can define a function using the 'def' keyword. Create
# a function called say_hello which does not take any arguments as parameters
# and simply prints "Hello" within the function. If this function were called
# it would print "Hello" to the screen. Note: No explicit return values.
## Write your code below

def say_hello():
    print("Hello")

# End question 1

# Question 2: Create a new function called say_hello_premium(). This will return
# the string "Hello" to the caller. Note: No print required.
## Write your code below

def say_hello_premium():
    return "Hello"

# End question 2

# Question 3: Create a new function called yell_message() which takes a string
# as an argument. Example def yell_message(some_string). This function takes
# the parameter some_string, and prints it out to the screen after using the
# upper method on it to capitalize all the letters in the string. Example, if
# you called the function like this: yell_message("lol"), the output to the
# screen would be LOL.
## Write your code below

def yell_message(some_string):
    print(some_string.upper())

# End question 3

##########################

# Question 1: Write a function called simple_mult. It takes 2 arguments
# as parameters and returns their multiplied value. Assume only numbers are
# passed in as arguments, so you don't have to test for if the parameters
# are numbers are not.
## Write your code below

def simple_mult(a,b):
    return a * b

# End question 1

# Question 2: Create a new function called simple_mult_premium(). This will
# take two numbers as parameters (int or float). You will need to check for if
# both the parameters passed in are either of type "int" or "float" and return
# their multiplied value if they are. If either of them are not "int" or "float"
# return the string "Need either int or float". You can use the isinstance
# function to test the type of the parameter. Example if you were testing num_1,
# you can use code like isinstance(num_1, (int, float)) to test for int or float.
# This expression will return True if num_1 is of type int or float (passed in
# as a tuple here). You can also do this individually like below
# isinstance(num_1, int)
## Write your code below

def simple_mult_premium(a,b):
    if isinstance(a, (int,float)) and isinstance(a, (int,float)):
        return a * b
    return "Need either int or float"

# End question 2

# Question 3: Create a new function called create_divider() which takes a string
# as an argument and multiplies it by 40 to create a line full of the string
# and prints it out to the screen. Example "-" * 10 would give you
# ---------- so you can then use this function later on to create dividers in
# your output if you wanted. Remember to multiply by 40 and not 10.
## Write your code below

def create_divider(p):
    return p*40

print(create_divider("*"))
# End question 3