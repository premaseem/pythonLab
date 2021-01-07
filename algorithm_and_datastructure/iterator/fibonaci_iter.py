# Fibonaci series implemented using iterator design pattern

class FibonaciIter:


    def __init__(self, n):
        self.n = n
        self.arr = [0,1]
        self.position = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.position += 1
        if self.position >= self.n:
            raise StopIteration
        if self.position == 0 :
            return 0
        if self.position == 1:
            return 1
        v = self.arr[self.position-2] + self.arr[self.position-1]
        self.arr.append(v)
        print(".")
        return v

print(list(FibonaciIter(10)))
