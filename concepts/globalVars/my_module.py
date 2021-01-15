__author__ = 'asee2278'
"""
Global keyword is a keyword that allows a user to modify a variable outside of the current scope. 
It is used to create global variables from a non-global scope i.e inside a function. 
Global keyword is used inside a function only when we want to do assignments or when we want to change a variable. 
Global is not needed for printing and accessing.
"""

Money = 2000
def AddMoney():
    # Uncomment the following line to fix the code:
    global Money
    Money =  Money + 1

print(Money)
AddMoney()
print(Money)


accountBalance=100
class Bank:

    accountBalance=10
    def deposit(self,amount):
        global accountBalance
        accountBalance = accountBalance + Money
        return accountBalance

print(Bank().deposit(20))