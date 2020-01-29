# pretty print a linked list
class Node():

    def __init__(self, data=None, next=None):
        self.data, self.next = data, next

    # This would recursively print linked list
    # sample output
    # 90,20,80,40,70,30,10,None
    def __str__(self):
        return str(self and self.data) + ',' + str(self and self.next)


class Stack():
    def __init__(s):
        s.head = None

    def push(self, e):
        self.head = Node(e, self.head)

    def pop(self):
        if self.head:
            n = self.head.next
            self.head = n
            return n

    def pretty_print(self):
        print(self.head)

stack = Stack()
stack.push(40)
stack.push(60)
stack.push(20)
stack.push(80)
stack.push(100)

stack.pretty_print()