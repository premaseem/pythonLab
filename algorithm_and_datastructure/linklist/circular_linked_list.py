# CIRCULAR LINKED LIST
# the tail node points to the head of the linked list instead of pointing to null which makes the linked list circular.

class Node():
    def __init__(self,value):
        self.value = value
        self.next = None

class CLL:
    def __init__(self):
        self.head = None
        # nn = Node(value)
        # self.head = nn
        # nn.next = nn

    def append(self,value):
        nn = Node(value)
        if not self.head:
            self.head = nn
            nn.next = nn
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next

        cur.next = nn
        nn.next = self.head
        # self.head = nn

    def prepend(self,value):
        nn = Node(value)
        if not self.head:
            self.head = nn
            nn.next = self.head
            return
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        curr.next = nn

        nn.next = self.head
        self.head = nn


    def print(self):
        print()
        cur = self.head
        # print(self.head.value)
        while cur.next != self.head:
            print(cur.value,"-",end=" ")
            cur = cur.next
        print(cur.value)

    def print2(self):
        print()
        cur = self.head
        while cur:
            print(cur.value,end=" - ")
            cur = cur.next
            if cur == self.head:
                break



cll = CLL()
cll.append(1)
cll.append(2)
cll.append(3)
cll.append(4)
cll.append(5)

cll.print2()
cll.prepend(100)
cll.print2()
