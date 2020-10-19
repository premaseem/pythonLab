
"""
first or lowermost implementation of method would be invoked
"""
class A:
    def __str__(self):
        return 'a'

class B(A):

    def __str__(self):
        return 'b'


class C(B):
    pass

o = C()
print(o)

##############
""" 
Multiple inheritance, evaluates left to right 
"""
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')


class C(B,A):
    def c(self):
        self.a()

o = C()
o.c()


##########

class A:
    def __str__(self):
        return 'a'

class B(A):
    def __str__(self):
        return 'b'


class C(B):
    pass

o = C()
print(o)
