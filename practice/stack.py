class Stack:
    def __init__(self):
        self.arr=[]
        self.ci=0

    def push(self,e):
        self.arr.append(e)
        self.ci += 1

    def pop(self):
        if len(self.arr) > 0:
            self.ci -= 1
            return self.arr.pop()

    def peek(self):
        if len(self.arr) > 0:
            return self.arr[self.ci]







