# Aseem Jain

## DEFINITION:
# Stacks follow the Last in First Out (LIFO) ordering. This means that the last element added is the element on the top and the first element added is at the bottom.

## ANALOGY
# A real-life example of Stack could be a stack of books. So, in order to get the book that’s somewhere in the middle, you will have to remove all the books placed at the top of it. Also, the last book you added to the stack of books is at the top!

## USAGE
# Reversing
# Undo functionality
# Depth First Search
# Expression Evaluation Algorithm

## FUNCTIONS

# push -> adds element on top
# pop -> pop out element on top
# top or peek -> element on top
# is_empty -> boolean
# size() -> current size of stack

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

    def remove_last(self):
        if not self.head:
            return

        c = self.head
        while c.next:
            c = c.next

        if self.head == c:
            self.head =None
        else:
            c.next = None
        return c.data

    def size(self):
        cnt = 0
        c = self.head
        while c:
            cnt += 1
            c = c.next
        return cnt

    def top(self):
        c = self.head
        while c.next:
            c = c.next
        return c.data

    def display(self):
        c = self.head
        while c:
            print(c.data , "->", end="")
            c = c.next


class StackLinkedList:
    """ Stack implementation using linked list needs linked list implementation """

    def __init__(self):
        self.ll = LinkedList()

    def push(self, e):
        self.ll.add(e)

    def pop(self):
            return self.ll.remove_last()

    def top(self):
        return self.ll.top()

    def size(self):
        return self.ll.size()

    def is_empty(self):
        return self.ll.size() == 0

    def display(self):
        self.ll.display()


s = StackLinkedList()
s.push(20)
print(s.top())
print(s.pop())
print(s.size())
print(s.is_empty())
s.push(120)
s.push(220)
s.display()














