class MyRange:
    def __init__(self,begin,end,step=1):
        self.begin = begin
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.begin < self.end:
            v = self.begin
            self.begin += self.step
            return v
        else:
            raise StopIteration

table_2 = MyRange(2,22,2)

# next element can be printed with next
print(next(table_2))
print(next(table_2))

# iter can be iterated by for loop
for e in MyRange(3,32,3):
    print(e, end = " - ")
print()

# iter can be converted to list or list iterator
print(list(table_2))