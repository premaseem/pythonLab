# Objective: check equality in string is and ==
# @Author:  Aseem Jain

val = "elasticsearch"

def check(v):
    if v is "elasticsearch":
        print("eqality using is ")
    if v == "elasticsearch":
        print("equliaty using ==")

check(val)

# output
# eqality using is
# equliaty using ==