"""
@Title: Dispatch Tables in Python
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/


How to use a quick dictionary lookup to run a function dynamically, instead of a slow, long, boring if-elif statement
The code is less and cleaner, more readable, and there is no need to add a long set of if-elif statements.

"""

def greet_gm():
    print("good morning ")

def greet_ge():
    print("good evening ")

def greet_gn():
    print("good night ")

def greet_gnoon():
    print("good after noon ")

greet_table = {
    "gm" : greet_gm,
    "ge" : greet_ge,
    "gn" : greet_gn,
    "gan" : greet_gnoon
}


i = input("what time of day is it?")
greet_table.get(i.strip())()

