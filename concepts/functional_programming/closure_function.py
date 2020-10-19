"""
The closure contains enclosed scope of function.
with the init variable,

"""

class Mul:
    def __init__(self,m):
        self.m = m 
    
    def multiply_with(self, x):
        print(self.m * x)
        return self.m * x

m = Mul(2)
m.multiply_with(100)


def multiplier_of(m):
    inner_scope = m
    def multiply_with(x):
        print(inner_scope * x)
        return inner_scope * x

    return multiply_with


multiplier_obj = multiplier_of(5)
multiplier_obj(10)
multiplier_obj(5)
multiplier_obj(20)


def pure_func(x):
    print("value of x ", x)


pure_func(12)
pure_func(10)
pure_func(8)
