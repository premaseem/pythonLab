# Objective: check equality in string is and ==
# @Author:  Aseem Jain
# is checks object reference equality
# == checks value equality defined by __eq__

val = "elasticsearch"

def check(v):
    if v is "elasticsearch":
        print("eqality using is ")
    if v == "elasticsearch":
        print("equliaty using ==")

check(val)

class Price:
    def __init__(self,price):
        self.price = price
    def __eq__(self, other):
        print("invoked with")
        return self.price == other.price
# output
itema = Price(4)
itemb = Price(4)

print("eqality using is", itema is itemb)
print("equliaty using ==", itema == itemb)