# In Python, you can pass in functions as arguments to other functions.
# I have a function below that takes a function and a list as an argument and runs the function using the list as a parameter.
def run_func(func_name, some_list):
    return func_name(some_list)


l1 = [6, 5, 4, 9, 10, 23, 12]
print(run_func(sorted, l1))

if "a" == "b":
    pass
