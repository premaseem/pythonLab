class MyRange:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        myArray = []
        for i in range(self.n): # from n to 0
            if i == 0 or i == 1:
                myArray.append(i) # adds the even number to the list
            else:
                myArray.append(myArray[i-2] + myArray[i-1])
        return myArray

myrange = MyRange(8)
print(myrange.next())
print(myrange.next())
for e in myrange:
    print(e)