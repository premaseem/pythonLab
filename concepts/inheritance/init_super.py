"""
when init is not defined in subclass, super class init is called
when init is defined in subclass, then super class init is not called. so super can be used.

"""

class A:
    def __init__(self):
        print(" A init called")

class B(A):
    def __init__(self):
        print("only b init")
        super().__init__()


o = B()
print(o)


