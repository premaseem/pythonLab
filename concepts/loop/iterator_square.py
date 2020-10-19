"""
The iterator will generate a series of square in the sequence
"""

class SquareIterator:
    def __init__(self, max):
        self.max = max

    def __iter__(self):
        self.pointer = 1
        return self

    def __next__(self):
        num = self.pointer ** 2
        if self.pointer > self.max:
            raise StopIteration
        self.pointer += 1
        return num


o = SquareIterator(5).__iter__()
try :
    while True:
        print(o.__next__())
except :
    pass


print([ x for x in SquareIterator(5).__iter__() ] )
