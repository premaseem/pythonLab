class N():
    def __init__(self,data):
        self.data = data
        self.down = None


class MyStack():
    def __init__(self):
        self.sp = None

    def push(self,data):
        o = N(data)
        if self.sp is None:
            self.sp = o
            return
        o.down = self.sp
        self.sp = o


    def peek(self):
        return self.sp

    def pop(self):
        if not self.is_empty():
            self.sp = self.sp.down

    def is_empty(self):
        return self.sp is None

    def __str__(self):
        o = self.sp
        s =""
        while o is not None:
            s = s + str(o.data) + "\n"
            s = s + "--- \n"
            o = o.down
        return s

if __name__ == "__main__":
    my_stack = MyStack()
    for i in range(10):
        my_stack.push(i)
    print(my_stack)
    my_stack.pop()
    print(my_stack)
