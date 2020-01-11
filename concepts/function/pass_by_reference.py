# Pass by Reference vs Value
# All parameters (arguments) in the Python language are passed by reference. It means if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example −

# !/usr/bin/python3

# Function definition is here
def changeme(mylist):
    "This changes a passed list into this function"
    print("Values inside the function before change: ", mylist)

    mylist[2] = 50
    print("Values inside the function after change: ", mylist)
    return


# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)

# Output
# Values inside the function before change:  [10, 20, 30]
# Values inside the function after change:  [10, 20, 50]
# Values outside the function:  [10, 20, 50]