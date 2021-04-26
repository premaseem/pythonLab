class MyQueue:
    def __init__(self):
        self.arr = []

    def enqueue(self,n):
        self.arr(0,n)

    def dequeue(self):
        if not self.arr.isEmpty() :
            return self.arr.pop()

    def isEmpty(self):
        return len(self.arr) == 0

    def peek(self):
        return self.arr[-1]
