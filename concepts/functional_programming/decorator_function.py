"""
 Decorators are very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.
"""
import time


def time_decorator(func):

    def inner_func(*args, **kwargs):
        t_start = time.time()
        r = func(*args, **kwargs)
        t_stop = time.time()
        run_time = t_stop - t_start
        print(run_time)
        return r , run_time
    return inner_func

@time_decorator
def looper(max):
    for x in range(max):
        time.sleep(1)

print(looper(3))