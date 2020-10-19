
class A:
    pass
    # v = 1

class B(A):
    pass
    # v = 2


class C(B):
    pass
    v = 3

o = C()
print(o.v)



####

def f(x):
    try:
        x = x / x
    except:
        print("a",end='')
    else:
        print("b",end='')
    finally:
        print("c",end='')

f(1)
f(0)

try:
    raise Exception(1,2,3)
except Exception as e:
    print(len(e.args))


###

    class Ex(Exception):
        def __init__(self,msg):
            Exception.__init__(self,msg + msg)
            self.args = (msg,)

    try:
        raise Ex('ex')
    except Ex as e:
        print(e)
    except Exception as e:
        print(e)
