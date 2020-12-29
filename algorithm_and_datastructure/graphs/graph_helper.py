class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.visited = False

class LinkedList:

    def __init__(self):
        self.head = None

    def __len__(self):
        size = 0
        c = self.head
        while c:
            size += 1
            c = c.next
        return size

    def is_empty(self):
        return not self.head

    def add(self,data):
        nn = Node(data)
        if not self.head:
            self.head = nn
            return

        c = self.head
        while c.next:
            c = c.next
        c.next = self.head
        self.head = nn



    def display(self):
        if not self.head:
            return
        # print()
        c = self.head
        while c:
            print(c.data, " - ",end="")
            c = c.next
        # print()

    def remove(self,k):
        if not self.head:
            return

        if self.head.data == k:
            self.head = self.head.next
            return

        prev = None
        c = self.head
        while c.next:

            if c.data == k:
                prev.next = c.next
            prev = c
            c = c.next

        print()

class Q:
    def __init__(self):
        self.q = []

    def enqueue(self,n):
        self.q.insert(0,n)

    def dequeue(self):
        if len(self.q) > 0:
            return self.q.pop()

    def peek(self):
        return self.q[-1]

    def __len__(self):
        return len(self.q)

class Stack:
    def __init__(self):
        self.q = []

    def push(self,n):
        self.q.push(n)

    def pop(self):
        if len(self.q) > 0:
            return self.q.pop()

    def peek(self):
        return self.q[-1]

    def __len__(self):
        return len(self.q)






ll = LinkedList()

# print(ll.is_empty())
# ll.add(2)
# ll.add(3)
# ll.remove(2)
# ll.display()
