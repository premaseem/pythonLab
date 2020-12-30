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

class Node:
    def __init__(self, e):
        self.data = e
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, e):
        new_node = Node(e)
        if not self.head:
            self.head = new_node
            return
        c = self.head
        while c.next:
            c = c.next
        c.next = new_node

    def remove_first(self):
        if not self.head:
            return
        c = self.head
        self.head = self.head.next
        return c.data

    def size(self):
        cnt = 0
        c = self.head
        while c:
            cnt += 1
            c = c.next
        return cnt

    def front(self):
        if not self.head:
            return
        c = self.head
        while c.next:
            c = c.next
        return c.data

    def back(self):
        if not self.head:
            return
        return self.head.data

    def display(self):
        c = self.head
        while c:
            print(c.data , "->", end="")
            c = c.next



class QueueLinkedList:
    """ Queue implementation using array is straight forward as all
    operations are provided by array list """

    def __init__(self):
        self.ll = LinkedList()

    def enqueue(self, e):
        self.ll.add(e)

    def dequeue(self):
        return self.ll.remove_first()

    def front(self):
        return self.ll.front()

    def back(self):
        return self.ll.back()

    def size(self):
        return self.ll.size()

    def is_empty(self):
        return self.ll.size() > 0

    def display(self):
        self.ll.display()


s = QueueLinkedList()
s.enqueue(20)
print(s.front())
print(s.back())
print(s.dequeue())
s.enqueue(120)
print(s.size())
print(s.is_empty())
s.display()

















