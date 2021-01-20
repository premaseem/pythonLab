"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import time

def timeit(fun):
    def wrapper(*arg,**kwargs):
        st = time.time()
        ret = fun(arg,kwargs)
        et = time.time()
        delta = et -st
        print(delta)
        return ret
    return wrapper

@timeit
def candidate(*arg,**kwargs):
    print("start",arg)
    time.sleep(2)
    print("stop")

candidate("param")