from multiprocessing import Pool
import time

data = (
    ['a', '2'], ['b', '4'], ['c', '6'], ['d', '8'],
    ['e', '1'], ['f', '3'], ['g', '5'], ['h', '7']
)

def mp_worker(data):

    print (" Processs {} Waiting {} seconds".format(data[0], data[1]))
    time.sleep(int(data[1]))
    print (" Process %s\tDONE" % data[0])

def mp_handler():
    p = Pool(4)
    p.map(mp_worker, data)

if __name__ == '__main__':
    mp_handler()