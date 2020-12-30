# Aseem Jain

## DEFINITION:
# Queue is FIFO, the first element inserted is the one that comes out first. You can think of a queue as a pipe with both ends open. Elements enter from one end (back) and leave from the other (front).

## ANALOGY
# A perfect real-life example of a queue is a line of people waiting to get a ticket from the booth.

## FOUR TYPES OF QUEUE

# Linear Queue - Normal FIFO
# Circular Queue - both ends are connected to form a cirlce
# Priority Queue - high priority items are moved to front and low priority to back or rear end.
# Double-ended Queue - both ends could be used to enqueue and dequeue items.

## USAGE
# Tickets systems

## FUNCTIONS

# enqueue -> adds element to back or rear end
# dequeue -> pop out element from front
# front -> element in front
# back -> element in back
# is_empty -> boolean
# size() -> current size

# Run time complexity of all operations is Time O(1)


class QueueArray:
    """ Queue implementation using array is straight forward as all
    operations are provided by array list """

    def __init__(self):
        self.arr = []

    def enqueue(self, e):
        self.arr.insert(0, e)

    def dequeue(self):
        if self.arr:
            return self.arr.pop()

    def front(self):
        if self.arr:
            return self.arr[-1]

    def back(self):
        if self.arr:
            return self.arr[0]

    def size(self):
        return len(self.arr)

    def is_empty(self):
        return len(self.arr) == 0

    def display(self):
        print(self.arr)


s = QueueArray()
s.enqueue(20)
print(s.front())
print(s.back())
print(s.dequeue())
s.enqueue(120)
print(s.size())
print(s.is_empty())
s.display()

















