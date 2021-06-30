import multiprocessing
import time


def square(x):
    time.sleep(2)
    return x * x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    inputs = [0,1,2,3,4]
    outputs_async = pool.map_async(square, inputs)
    outputs = outputs_async.get()
    print(sum(outputs))
    print("Output: {}".format(outputs))
    print("main finished")


