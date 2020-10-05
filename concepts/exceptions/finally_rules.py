"""
Finally block would be called and would override any returns or excepts in the try block.

"""

def List(n):
    l = [0,1,2,3,4,5,6,7,8,9]
    try:
        raise Exception
        return l[:5]
    finally :
        return l[5:]
        print("after impact")
        pass
print(List(5))