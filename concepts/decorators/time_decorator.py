"""
This decorator will measure time of execution
:arg
"""

import time

def timetest(input_func):

    def timed(*args, **kwargs):

        start_time = time.time()
        result = input_func(*args, **kwargs)
        end_time = time.time()
        print ("Method Name - {0}, Args - {1}, Kwargs - {2}, Execution Time - {3}".format(
            input_func.__name__,
            args,
            kwargs,
            end_time - start_time
        ))
        return result
    return timed


@timetest
def foobar(*args, **kwargs):
    time.sleep(0.3)
    print ("inside foobar")
    print (args, kwargs)

foobar("hello, world", foo=2, bar=5)

# this means
# foobar = timetest(foobar)
# foobar = timed
# foobar(1,2,3) = timed(1,2,3)
# inside foobar
# (['hello, world'],) {'foo': 2, 'bar': 5}
# Method Name - foobar, Args - (['hello, world'],), Kwargs - {'foo': 2, 'bar': 5}, Execution Time - 0.30296087265