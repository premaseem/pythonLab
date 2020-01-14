# Welcome to the assessment test for Python basics.

# Question 1: Given the 4 numbers below, fill in the code
# for the 8 lines below to provide the appropriate output
num_1 = 10
num_2 = 300
num_3 = 27.0
num_4 = -10
print(f"Calculations section:\nnum_1-> {num_1}\nnum_2-> {num_2}\nnum_3-> {num_3}\nnum_4-> {num_4}")
print(f"{num_1} multiplied by {num_2} is: **fill in the code here**")
print(f"{num_3} divided by {num_1} is: {num_3 / num_1}")
print(f"If I use floor division instead I get: **fill in the code here**")
print(f"The absolute value of {num_4} is: {abs(num_4)}")
print(f"I converted {num_1} and {num_2} to strings, if I add them I get: **fill in the code here**")
print(f"{num_4} is of the **fill in the code here** class")
print("-"*40)
print()

# Question 2a: Use two tabs to separate the evaluated variables in the string
# below. Example output-> Added:     Price updater
#                         Begin:     17:30:00
#                         End:       18:30:00
name_of_job = "Price updater"
begin_time = "17:30:00"
end_time = "18:30:00"
print(f"Added: \t{name_of_job}")
print(f"Begin: \t{begin_time}")
print(f"End: \t{end_time}")
print("-"*40)
print()

# Question 2b: Use new lines in addition to the two tabs noted above to
# separate the evaluated variables in the string below.
# Example output-> Added:     Price updater
#                  Begin:     17:30:00
#                  End:       18:30:00
print(f"Added: \t{name_of_job} \nBegin: \t{begin_time} \nEnd: \t{end_time}")
print("-"*40)
print()

# Question 3: Use the .format method to update the line below
print(name_of_job, "scheduled to begin at", begin_time, "and end at", end_time)
print(" {} scheduled to begin at {}  and end at {}".format(name_of_job,begin_time, end_time))
print("-"*40)
print()

# Question 4: Use the pow function from math module to evaluate 2 to the
# power of 5, or 2^5
import math
print("2 to the power of 5 is listed below...")
print(2**5)
print("-"*40)
print(math.pow(2,5))

# Question 5: Use the log2 function from math module to evalute log base 2
# of 32
print("log base 2 of 32 is listed below...")
print(math.log2(32))
print("-"*40)
print()

# Question 6: Use slicing notation to print the last 6 letters of the string
# below. Assume you donot know the start index or the length of the string upfront.
# Hint: You will need to use a function to find the length first and then use that,
# in combination with the number to come up with the start index
welcome_message = "Hello and welcome to the land of Python"
l= len(welcome_message)
print(f"The last 6 letters of the welcome message:\n'{welcome_message}'\nare: {welcome_message[l-7:l]}")
